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

def main():
    print("Welcome to Pass Craft Password Generator!")

    while True:
        try:
            num_passwords = int(input("How many passwords would you like to generate? "))
            if num_passwords <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Please enter a valid integer.")
