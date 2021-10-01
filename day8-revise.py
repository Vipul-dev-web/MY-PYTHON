import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

what_to_do = input(
    "Type \"encode\" for encryption and \"decode\" for decryption\n")
message = input("Enter your text here: \n").lower()
shift = int(input("Enter the shift you want: \n"))


def change_text(plain_text, i):
    new_text = ""
    if what_to_do == "encode":
        shift_num = i
    elif what_to_do == "decode":
        shift_num = i * -1

    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_num
        new_text += alphabet[new_position]

    print(f"The {what_to_do}d text is : {new_text}")


change_text(message, shift)
