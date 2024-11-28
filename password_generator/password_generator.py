import random
import string

def generate_password(min_length, number= True, special_char = True):
    letter = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters = letter
    if number:
        characters+= digits
    if special_char:
        characters+= special
    pwd = ''
    meets_critaria = False
    has_number = False
    has_special = False

    while not  meets_critaria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
          
        meets_critaria = True 
        if number:
            meets_critaria = has_number
        if special_char:
            meets_critaria = meets_critaria and has_special
    return pwd    
min_length = int(input('Enter the minimun lenth: '))
has_number = input('Do you want to have a number(y/n)? ').lower() == 'y'
has_special = input('Do you want to have special characters(y/n)? ').lower() == 'y'
pwd= generate_password(min_length, has_number, has_special)
print (pwd)  
