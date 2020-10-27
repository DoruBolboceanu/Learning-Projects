#Importing the necessary module for advanced math operations
import math
 
#While loop for continuously running the program and allowing the user to always go back to the main menu and choose another option
while True:
    #The user picks the math operation from the menu (we use \n to insert a new row in the menu)
    print("\nChoose the math operation.\n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a power\n6 - Square root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")
 
    oper = input("\nYour option from the menu: ") #The variable that saves the option chosen by the user
 
    #Addition
    if oper == "0":
        val1 = float(input("\nFirst value: ")) #The variable storing the first value, converted from string to float
        val2 = float(input("\nSecond value: ")) #The variable storing the second value, converted from string to float
 
        print("\nThe result is: " + str(val1 + val2) + "\n")
 
        #Going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
 
        if back == 'y':
            continue
        else:
            break
 
    #Subtraction
    elif oper == "1":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
 
        print("\nThe result is: " + str(val1 - val2) + "\n")
 
        #Going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
 
        if back == 'y':
            continue
        else:
            break
 
    #Multiplication
    elif oper == "2":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
 
        print("\nThe result is: " + str(val1 * val2) + "\n")
 
        #Going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
 
        if back == 'y':
            continue
        else:
            break
 
    #Division
    elif oper == "3":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
 
        print("\nThe result is: " + str(val1 / val2) + "\n")
 
        #Going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
 
        if back == 'y':
            continue
        else:
            break
 
    #Modulo
    elif oper == "4":
        val1 = float(input("\nFirst value: "))
        val2 = float(input("\nSecond value: "))
 
        print("\nThe result is: " + str(val1 % val2) + "\n")
 
        #Going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
 
        if back == 'y':
            continue
        else:
            break
 
    #Raising to a power
    elif oper == "5":
        val1 = float(input("\nEnter the base: "))
        val2 = float(input("\nEnter the power: "))
 
        print("\nThe result is: " + str(math.pow(val1, val2)) + "\n")
 
        #Going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
 
        if back == 'y':
            continue
        else:
            break
 
    #Square root
    elif oper == "6":
        val1 = float(input("\nEnter value for extracting the square root: "))
 
        print("\nThe result is: " + str(math.sqrt(val1)) + "\n")
 
        #Going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
 
        if back == 'y':
            continue
        else:
            break
    
    #Logarithm
    elif oper == "7":
        val1 = float(input("\nEnter the value for calculating the logarithm to base 2: "))
 
        print("\nThe result is: " + str(math.log(val1, 2)) + "\n")
 
        #Going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
 
        if back == 'y':
            continue
        else:
            break
    
    #Sine
    elif oper == "8":
        val1 = float(input("\nEnter the value (in degrees) for calculating the sine: "))
 
        print("\nThe result is: " + str(math.sin(math.radians(val1))) + "\n")
 
        #Going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
 
        if back == 'y':
            continue
        else:
            break
 
    #Cosine
    elif oper == "9":
        val1 = float(input("\nEnter the value (in degrees) for calculating the cosine: "))
 
        print("\nThe result is: " + str(math.cos(math.radians(val1))) + "\n")
 
        #Going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
 
        if back == 'y':
            continue
        else:
            break
 
    #Tangent
    elif oper == "10":
        val1 = float(input("\nEnter the value (in degrees) for calculating the tangent: "))
 
        print("\nThe result is: " + str(math.tan(math.radians(val1))) + "\n")
 
        #Going back to the main menu or exiting the program
        back = input('\nGo back to the main menu? (y/n) ')
 
        if back == 'y':
            continue
        else:
            break
    
	#Handling invalid options
    else:
        print("\nInvalid option!\n")
        continue
 
#End of the program