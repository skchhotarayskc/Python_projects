import random

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','&','*','_','+']

print("Welcome to Random Password generator!")
nr_letters = int(input("How many letters would you like in your password : "))
nr_numbers = int(input("How many numbers would you like : "))
nr_symbols = int(input("How many symbols would you prefer : "))

password_list = []

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))

for num in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for sym in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ""
for pas in password_list:
    password += pas

print(f"Here is your password : {password}")