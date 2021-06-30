
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

# direction = "decode"
# text = "mjqqt"
# shift = 5

def caesar(input_text, shift_amount, input_direction):
    new_text = ""
    for letter in input_text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift_amount
        elif direction == "decode":
            new_position = position - shift_amount

        new_text += alphabet[new_position]

    print(f"The {input_direction}d text is {new_text}")


# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(input_text=text, shift_amount=shift, input_direction=direction)
