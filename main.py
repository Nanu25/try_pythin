"""
This will be a password generator with different simbol, letter, and numbers
"""

import math
import random
import string

def random_letter() -> str:
    return random.choice(string.ascii_letters)

def random_symbol() -> str:
    return random.choice(string.punctuation)

def random_number() -> str:
    return random.choice(string.digits)

def initial_password() -> list:
    password.append(random_letter())
    password.append(random_letter())
    password.append(random_symbol())
    password.append(random_symbol())
    password.append(random_number())
    password.append(random_number())

print("Tell what's the lenght of the password. The minimum lenght is 6 ")
n = int(input(">"))

password = []
initial_password()

for i in range(len(password), n):
    if i % 2 == 1:
        password.append(random_letter())
    else:
        password.append(random_number())

random.shuffle(password)

result = ""
for symbol in password:
    result += symbol

print(result)
