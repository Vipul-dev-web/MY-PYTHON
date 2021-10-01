# # import math
# # width_num = int(input("Enter width: "))
# # height_num = int(input("Enter height: "))
# # coverage = int(input("Enter coverage: "))


# # def num_cans(width, height, cover):
# #     area = width * height
# #     cans = math.ceil(area / cover)
# #     cans_abs = "{:.2f}".format(cans)
# #     print(f"Number of cans required {cans_abs}")


# # num_cans(width_num, height_num, coverage)


# # check_prime()
# def check_prime(num):
#     is_prime = True
#     for i in range(2, num):
#         if num % 1 == 0:
#             is_prime = False

#     if is_prime:
#         print("Prime")
#     else:
#         print("Not Prime")


# n = int(input("Enter the number"))
# check_prime(n)

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
#             'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")

# # TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.


# def decrypt(plain_text, shift_amount):
#     simple_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         simple_text += alphabet[new_position]
#     print(f"The encoded text is {simple_text}")

#     # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
#     # e.g.
#     #cipher_text = "mjqqt"
#     #shift = 5
#     #plain_text = "hello"
#     # print output: "The decoded text is hello"


# # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(plain_text=text, shift_amount=shift)
# else:
#     print("INVALID INPUT")


# final version

import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # TODO-3: What happens if the user enters a number/symbol/space?
        # Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
        #e.g. start_text = "meet me at 3"
        #end_text = "•••• •• •• 3"
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")

# TODO-1: Import and print the logo from art.py when the program starts.

# TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
# e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
# If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
# Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
# Try running the program and entering a shift number of 45.
# Add some code so that the program continues to work even if the user enters a shift number greater than 26.
# Hint: Think about how you can use the modulus (%).
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

run_cipher = input("Type 'yes' if you want to go again. Otherwise type 'no'")

while run_cipher == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
