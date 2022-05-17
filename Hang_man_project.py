import random

logo = ['''
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                       
''']

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''','''
  +---+
  |   |
      |
      |
      |
      |
=========
''','''
  +---+
      |
      |
      |
      |
      |
=========
''']

word_list = ["Apple", "Orange", "Banana", "Grapes", "Gwava", "Watermillon", "Apricots", " Avocados", "Cherries", "Dates", "Dragon Fruit", "Blueberries"]

choosen_word = random.choice(word_list).lower()

print(logo[0])

new_list = []
for n in choosen_word:
    new_list.append("_")
print(new_list)

no_of_lives = 7
j = 7
while no_of_lives > 0:
    guess = input("Choose a letter : ").lower()
    i = 0

    if guess in new_list:
        print(f"You already guessed {guess}")

    if guess not in choosen_word:
        no_of_lives -= 1
        print(f"You guessed '{guess}' that is not in the word, You lose a life")
        print(f"Now you have {no_of_lives} lives")
        j -= 1     
    print(stages[j])

    for letter in choosen_word:
        if letter == guess:
            new_list[i] = guess
        i += 1
    print(new_list)

    if "_" not in new_list:
        print("You Won!")
        break

if no_of_lives == 0:
    print("You lose")