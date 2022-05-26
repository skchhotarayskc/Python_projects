from random import randint

logo = '''
                              __                         
 |\ |     ._ _  |_   _  ._   /__      _   _  _ o ._   _  
 | \| |_| | | | |_) (/_ |    \_| |_| (/_ _> _> | | | (_| 
                                                      _| 
'''

no_of_lives = 0
while input("Type 'yes' to start a new game or 'no' to exit : ") == "yes":
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 to 100.")
    guessed_no = randint(1, 100)
    difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard' : ")

    if difficulty_level == "easy":
        no_of_lives = 10
    elif difficulty_level == "hard":
        no_of_lives = 5
    
    while no_of_lives > 0:
        print(f"You have {no_of_lives} attempts remaining to guess the number")
        users_guessed = int(input("Make a guess : "))

        if users_guessed > guessed_no:
            print("Too high.\nGuess again.")
            no_of_lives -= 1
        elif users_guessed < guessed_no:
            print("Too low.\nGuess again.")
            no_of_lives -= 1
        else:
            print(f"You got it! The answer was {guessed_no}")
            break
    
    if no_of_lives == 0:
        print("You run out of guesses, you lose.")