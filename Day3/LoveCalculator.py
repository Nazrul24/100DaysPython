# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
T = name1.count('t') + name2.count('t')
R = name1.count('r') + name2.count('r')
U = name1.count('u') + name2.count('u')
E = name1.count('e') + name2.count('e')

L = name1.count('l') + name2.count('l')
O = name1.count('o') + name2.count('o')
V = name1.count('v') + name2.count('v')

result = (T+R+U+E) * 10 + L+O+V+E

if result<10 or result>90:
    print(f"Your score is {result}, you go together like coke and mentos.")

elif result>=40 and result<=50:
    print(f"Your score is {result}, you are alright together.") 

else:
    print(f"Your score is {result}.")



