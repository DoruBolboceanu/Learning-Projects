from tkinter import *
from math import *
#Creating the functions for the buttons
expr = ''
def press(num):
    global expr
    expr = expr + str(num)
    eq.set(expr)

def clear():
    global expr
    expr = ''
    eq.set(expr)

def equals():
    try:
        global expr
        total = eval(expr)
        eq.set(total)
    except:
        eq.set("Sintaxa nu e corecta")
        
if True:
    gui = Tk()
    gui.title("Scientific Calculator")

    #creating the frame
    frame = Frame(gui, bg ='black')
    frame.grid()

    #Creating the GUI
    eq = StringVar()
    entry = Entry(frame, textvariable = eq, font=('arial', 14), bg='black', fg='white', width=38)
    entry.grid(row=0, columnspan=7)

    btn_id = "(,),del,%,rad,pi,e,7,8,9,x,sin,cos,tan,4,5,6,-,ln,log,1/x,1,2,3,+,e^x,x^2,x^y,Clear,0,.,=,|x|,sqrt,x!".split(',')
    btn_cmd = "(,),del,%,radians(,pi,e,7,8,9,*,sin(,cos(,tan(,4,5,6,-,log(,log10(,1/,1,2,3,+,e**,^2,^,Clear,0,.,=,|x|,sqrt(,factorial(".split(',') 
    btn = []
    i = 0

    for k in [1,2,3,4,5]:
        for j in range(7):
            if i==btn_id.index('Clear'):
                btn.append(Button(frame, height=1, width=4, text=btn_id[i],
                fg='white', bg='grey12', font=('arial',12,'bold'), command=lambda:clear()))
                btn[i].grid(row=k, column=j, sticky=W)
            elif i==btn_id.index('='):
                btn.append(Button(frame, height=1, width=4, text=btn_id[i],
                fg='white', bg='grey12', font=('arial',12,'bold'), command=lambda:equals()))
                btn[i].grid(row=k, column=j, sticky=W)
            else:   
                btn.append(Button(frame, height=1, width=4, text=btn_id[i],
                fg='white', bg='grey12', font=('arial',12,'bold'), command=lambda i=i:press(btn_cmd[i])))
                btn[i].grid(row=k, column=j, sticky=W)
            i=i+1
               
    gui.mainloop()
