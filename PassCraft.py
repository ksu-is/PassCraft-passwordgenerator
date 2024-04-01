import string
import random

def generate_password(length, choices):
    characterList = ''
    for choice in choices:
        if choice == '1':
            characterList += string.digits
        elif choice == '2':
            characterList += string.ascii_letters
        elif choice == '3':
            characterList += string.punctuation
    password = [random.choice(characterList) for _ in range(length)]
    return ''.join(password)
