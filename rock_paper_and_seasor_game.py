import random

rock = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''']

paper = ['''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
''']

seasor = ['''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

print("Welcome to rock, paper, and seasor game!")


choice = ""
while choice != 4:

    print("What do you choose? Type 1 for Rock, 2 for paper or 3 for seasor and 4 to exit: ", end='')

    choice = int(input())
    computer_choice = random.randint(1, 3)

    if choice == 4:
        exit()

    if (choice == 1 and computer_choice == 1) or (choice == 2 and computer_choice == 2) or (choice == 3 and computer_choice == 3):
        print("Match draw")

    elif choice >= 4 or choice <= 0:
        print("You entered an invalid number. You lose")
        
    else:
        if choice == 1 and computer_choice == 2 :
            print("You choose rock.")
            print(rock[0])
            print("computer choose paper.")
            print(paper[0])
            print("You lose!")
        elif choice == 1 and computer_choice == 3 :
            print("You choose rock.")
            print(rock[0])
            print("computer choose seasor.")
            print(seasor[0])
            print("You won!")

        elif choice == 2 and computer_choice == 1 :
            print("You choose paper.")
            print(paper[0])
            print("computer choose rock.")
            print(rock[0])
            print("You won!")
        elif choice == 2 and computer_choice == 3 :
            print("You choose paper.")
            print(paper[0])
            print("computer choose seasor.")
            print(seasor[0])
            print("You lose!")
        
        elif choice == 3 and computer_choice == 1 :
            print("You choose seasor.")
            print(seasor[0])
            print("computer choose rock.")
            print(rock[0])
            print("You lose!")
        elif choice == 3 and computer_choice == 2 :
            print("You choose seasor.")
            print(seasor[0])
            print("computer choose paper.")
            print(paper[0])
            print("You won!")
