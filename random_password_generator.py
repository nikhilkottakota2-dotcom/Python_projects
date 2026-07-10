#random password generator
import random

words = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

numbers = ['1','2','3','4','5','6','7','8','9']

symbols = ['@','#','%','$','₹']

in_words = int(input("Enter the number of words password should have:"))
in_symbols = int(input("Enter number of symbols password should have:"))
in_numbers = int(input("Enter the number of numbers password should have:"))
password = ""
for ch in range(1,in_words+1):
    password += random.choice(words)
for number in range(1,in_numbers+1):
    password += random.choice(numbers)
for symbol in range(1,in_symbols+1):
    password += random.choice(symbols)
    password_shuffle = list(password)
    random.shuffle(password_shuffle)
    password = "".join(password_shuffle)
print(password)
