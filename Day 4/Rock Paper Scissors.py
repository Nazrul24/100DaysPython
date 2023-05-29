rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random




while(1):
    computer = random.randint(0,2)
    you = int(input("What do you choose? Type 0 Rock, 1 for Paper or 2 for Scissors : "))
    

    if you == 0:
        print("You chose")
        print(rock)
        if computer == 1:
            print("Computer chose")
            print(paper)
            print("You Lose")
        elif computer == 2:
            print("Computer chose")
            print(scissors)
            print("You Win")
        else :
            print("Computer chose")
            print(rock)
            print("Draw")

    elif you == 1:
        print("You chose")
        print(paper)
        if computer == 2:
            print("Computer chose")
            print(scissors)
            print("You Lose")
        elif computer == 0:
            print("Computer chose")
            print(rock)
            print("You Win")
        else :
            print("Computer chose")
            print(paper)
            print("Draw")
    elif you == 2:
        print("You chose")
        print(scissors)
        if computer == 0:
            print("Computer chose")
            print(rock)
            print("You Lose")
        elif computer == 1:
            print("Computer chose")
            print(paper)
            print("You Win")
        else :
            print("Computer chose")
            print(scissors)
            print("Draw")
            
    retry = input("If you want to play again press Y else press N : ")
    retry = retry.lower()
    if(retry == 'n'):
        break
