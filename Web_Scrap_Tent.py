from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import Workbook
import openpyxl
from openpyxl.styles import *



#acces page www.nootkasport.ro and get info from here
r_nootka = requests.get('https://www.nootkasport.ro/corturi/corturi-ultrausoare--46.htm&CF=1&Nr_persoane=2')

content_nootka = r_nootka.content
soup_nootka = BeautifulSoup(content_nootka, features="html.parser")

alls_nootka=[]
for d in soup_nootka.findAll('div', attrs={'class':'product_small_box_container'}):
    
    ##identify the name of the tent
    n = d.find('div', attrs={'class':'pbs_product_title'})
    name = n.findAll('a', title=True)[0]['title']
    
    ##identify the link to each tent
    link = n.findAll('a', href=True)[0]['href']
    
    ##identify the price of the ten
    price=[]
    p = d.find('div', attrs={'class':'product_price'})
    if p is not None:
        price.append(p.text)
    else:
        price.append(d.find('div', attrs={'class':'product_price_nopromo'}).text)
    #price column has some aditional characters like currency and 'de la '; we need to get rid of those and just have plain number
    price = str(price)
    price = price[2:-5]
    if price.startswith('de la '):
        price=price[5:]

    ##getting each detailed page from each tent
    r_link = requests.get(link)
    content_link = r_link.content
    soup_link = BeautifulSoup(content_link, features="lxml")
    ##Adding weight of tent in the excel table; the code search the part with the weight, makes it as string and then searches for the value
    greutate = str(soup_link.findAll('div', attrs={'class':'product_detail_container'}))
    pos_greutate = greutate.find('kg')
    greutate = greutate[pos_greutate-8:pos_greutate+2]
    greutate = greutate[greutate.find(" "):greutate.find('kg')]
    

    ##Group all parameters of tent (name, price, link, weight into list(result))
    result = name.startswith('Cort')
    if result == True:
        alls_nootka.append(name)
        alls_nootka.append(price)
        alls_nootka.append(greutate)
        alls_nootka.append(link)
        
        

#print(alls_nootka)

#acces www.mormota.ro
r_mormota = requests.get('https://mormota.ro/corturi/corturi/corturi-extremlight.html?nr_persoane=672')
content_mormota = r_mormota.content
soup_mormota = BeautifulSoup(content_mormota,"lxml")

alls_mormota=[]
for d_mormota in soup_mormota.findAll('li', attrs={'class':'item product product-item'}):
    n_mormota = d_mormota.find('strong', attrs={'class':'product name product-item-name'})
    name_mormota = n_mormota.text
    name_mormota = name_mormota
    link_mormota = n_mormota.findAll('a', href=True)[0]['href']
    pret_mormota = d_mormota.find('span', attrs={'class':'price'})
    pret_mormota = pret_mormota.text
    
    ##the price string has additional characters like 'lei' and ',' as delimiter for 1000. We deleted them to make plain number
    pret_mormota = pret_mormota[:-7]
    pret_mormota = pret_mormota.replace('.','')

    ##get the wieght of the tents
    r_link_mormota = requests.get(link_mormota)
    content_link_mormota = r_link_mormota.content
    soup_link_mormota = BeautifulSoup(content_link_mormota, features="lxml")
    
    greutate_mormota = str(soup_link_mormota.findAll('div', attrs={'class':'additional-attributes-wrapper'}))
    if greutate_mormota.find('kg')!=-1:
        pos_greutate = greutate_mormota.find('kg')
    elif greutate_mormota.find('Kg')!=-1:
        pos_greutate = greutate_mormota.find('Kg')
    
    greutate_mormota = greutate_mormota[pos_greutate-6:pos_greutate]
    greutate_mormota = greutate_mormota[greutate_mormota.find('>')+1:pos_greutate]
    greutate_mormota = greutate_mormota.replace(',','.')
    
    ##Getting watter resistance for the floor and exterior cover; it's a bit complicated, will be updated
    detalii_mormota = str(soup_link_mormota.findAll('div', attrs={'class':'additional-attributes-wrapper'}))
    pos_pod_mormota = detalii_mormota.find('data-th="Rezistenta apa folie sol (mm H2O)"')
    len_pod_mormota = len('data-th="Rezistenta apa folie sol (mm H2O)"')
    podea_mormota = detalii_mormota[pos_pod_mormota+len_pod_mormota:pos_pod_mormota+len_pod_mormota+15]
    podea_mormota = podea_mormota.replace(' ','')
    x = podea_mormota.count('0')
    podea_mormota = podea_mormota[1:x+2]

    pos_fol_mormota = detalii_mormota.find('data-th="Rezistenta apa folie exterioara (mm H2O)"')
    len_fol_mormota = len('data-th="Rezistenta apa folie exterioara (mm H2O)"')
    fol_mormota = detalii_mormota[pos_fol_mormota+len_fol_mormota:pos_fol_mormota+len_fol_mormota+10]
    fol_mormota = fol_mormota.replace(' ','')
    y = fol_mormota.count('0')
    fol_mormota = fol_mormota[1:y+2]
    

    alls_mormota.append(name_mormota)
    alls_mormota.append(pret_mormota)
    alls_mormota.append(greutate_mormota)
    alls_mormota.append(link_mormota)
    

alls = alls_nootka+alls_mormota   

nm=[]
pr=[]
ln=[]
gr=[]
for i in range(int(len(alls)/4)):
    nm.append(alls[4*i])
    pr.append(alls[4*i+1])
    gr.append(alls[4*i+2])
    ln.append(alls[4*i+3])

df = pd.DataFrame({'Nume': nm,
                   'Pret': pr,
                   'Greutate': gr,
                   'Link':ln})

df.to_excel('Cort.xlsx',index=False)

## aranging the excel file, make it nicer
path = 'C:\\Users\\Clatita_Atomica\\Desktop\\Python\\Applications\\Web_Scrapp_Tent\\Cort.xlsx'
workbook = openpyxl.load_workbook('C:\\Users\\Clatita_Atomica\\Desktop\\Python\\Applications\\Web_Scrapp_Tent\\Cort.xlsx')
sheet = workbook['Sheet1']
A1 = sheet['A1']
B1 = sheet['B1']
C1 = sheet['C1']
D1 = sheet['C1']

font = Font(name='Calibri',size=13,bold=True,italic=False)
(A1.font, B1.font, C1.font, D1.font) = (font,font,font,font)
sheet1 = workbook.get_sheet_by_name('Sheet1')

for row in sheet1['D2':'D200']:
    for cell in row:
        ob = cell.value
        cell.hyperlink = ob
        cell.style = 'Hyperlink'
        cell.value = 'Link'

workbook.save(path)