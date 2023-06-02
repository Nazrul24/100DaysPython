# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passwordLen = nr_letters + nr_numbers + nr_symbols
password = ""

for i in range(0,passwordLen):
    choice = random.randint(0,2)
    if (choice==0):
        if(nr_letters>0):
            ch = random.randint(0,51)
            x = letters[ch]
            password = password + x
            nr_letters-=1
        elif(nr_symbols>0):
            ch = random.randint(0,8)
            x = symbols[ch]
            password = password + x
            nr_symbols-=1
        else:
            ch = random.randint(0,9)
            x = numbers[ch]
            password = password+x
            nr_numbers-=1

    elif (choice==1):
        if(nr_symbols>0):
            ch = random.randint(0,8)
            x = symbols[ch]
            password = password + x
            nr_symbols-=1

        elif(nr_letters>0):
            ch = random.randint(0,51)
            x = letters[ch]
            password = password + x
            nr_letters-=1
        
        else:
            ch = random.randint(0,9)
            x = numbers[ch]
            password = password+x
            nr_numbers-=1
    else:
        if (nr_numbers>0):
            ch = random.randint(0,9)
            x = numbers[ch]
            password = password+x
            nr_numbers-=1
    
        elif(nr_symbols>0):
            ch = random.randint(0,8)
            x = symbols[ch]
            password = password + x
            nr_symbols-=1

        else:
            ch = random.randint(0,51)
            x = letters[ch]
            password = password + x
            nr_letters-=1

print("The generated password : "+password)
        
    
