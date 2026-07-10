# cieser ciper 
# this program is used to encrypt and decrypt the data in this the encryption is done by shifting the alphaberts
#example : we have a,b,c,d we shifts if 2 then it is encrypted to bcde

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' for encrypt and 'decode' for decrypt:")
text = input("Enter your message:").lower()
shifts = int(input("Enter how many shifts:"))

def encrypt(original_text,shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter)+shift_amount
        cipher_text += alphabet[shifted_position]

    print(f"Here is the encrypted word:  {cipher_text}")
def decrypt(original_text,shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter)-shift_amount
        cipher_text += alphabet[shifted_position]

    print(f"Here is the encrypted word:  {cipher_text}")

if direction == "encode":
    encrypt(text,shifts)
elif direction == "decode":
    decrypt(text,shifts)
else:
    print("Check the direction you gave")