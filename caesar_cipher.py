alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

logo = ['''
    .d8888b. .d8888b. .d8888b. .d8888b. .d8888b. 88d888b. 
    88'  `"" 88'  `88 88ooood8 Y8ooooo. 88'  `88 88'  `88 
    88.  ... 88.  .88 88.  ...       88 88.  .88 88       
    `88888P' `88888P8 `88888P' `88888P' `88888P8 dP       
                                                        
                                                        
            oo          dP                               
                        88                               
    .d8888b. dP 88d888b. 88d888b. .d8888b. 88d888b.       
    88'  `"" 88 88'  `88 88'  `88 88ooood8 88'  `88       
    88.  ... 88 88.  .88 88    88 88.  ... 88             
    `88888P' dP 88Y888P' dP    dP `88888P' dP             
                88                                        
                dP                                        
''']

print(logo[0])

def encrypt(plain_text, shift_amount):
    cipher_text = ''

    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter) 
            cipher_text += alphabet[position + shift_amount]
        else:
            cipher_text += letter

    return cipher_text

def decrypt(encrypted_text, shift_amount):
    decrypted_text = ''

    for letter in encrypted_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            decrypted_text  += alphabet[position-shift_amount]
        else:
            decrypted_text += letter
    
    return decrypted_text

message = "yes"

while message != "no":

    direrction = input("Type 'encode' to encrypt and 'decode' to decrypt : ")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number : "))
    shift %= 25

    if direrction == "encode":
        print(f"Here is your encoded message : {encrypt(plain_text=text, shift_amount=shift)}")
    elif direrction == "decode":
        print(f"The decoded message is : {decrypt(encrypted_text=text, shift_amount=shift)}")
    
    message = input("Type 'yes' to continue and 'no' to exit : ")