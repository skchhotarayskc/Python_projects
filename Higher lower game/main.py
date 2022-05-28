from os import system
from art import logo , vs
from game_data import data
import random

def format_account(account):
    '''Takes the account data and returns the printable format'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    '''Takes the users guess and followers count and returns if they got it right'''
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

is_user_correct = True
correct_count = 0
account_b = random.choice(data)

while is_user_correct:

    # Display art
    system('CLS')
    print(logo)

    # Generate a random account from the game data
    account_a = account_b
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_account(account_a)}.")
    print(vs)
    print(f"Against B: {format_account(account_b)}.")

    # Ask user for a guess
    users_choice = input("Who has more followers? Type 'A' or 'B' : ").lower()

    # Check if user is correct
    ## Get follower count for each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    
    is_user_correct = check_answer(users_choice, a_follower_count, b_follower_count)
    
    if is_user_correct == True:
        correct_count += 1
        print(f"You are right and your score is {correct_count}")
        

system('CLS')
print(logo)
print("Sorry that's wrong")
print(f"Your final score is {correct_count}")