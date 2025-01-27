from ascii_art import ascii_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(original_text, shift_amount):
    encoded_text = ""
    for i in original_text:
        if i in alphabet:
            new_position = (alphabet.index(i) + shift_amount) % len(alphabet)
            encoded_text += alphabet[new_position]
        else:
            encoded_text += i
    print(f"The encoded text is: {encoded_text}")

def decrypt(original_text, shift_amount):
    decoded_text = ""
    for i in original_text:
        if i in alphabet:
            new_position = (alphabet.index(i) - shift_amount) % len(alphabet)
            decoded_text += alphabet[new_position]
        else:
            decoded_text += i
    print(f"The decoded text is: {decoded_text}")

print(ascii_art)

while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
    if direction not in ["encode", "decode"]:
        print("Invalid option. Please type 'encode' or 'decode'.")
        continue

    shift_amount = int(input("Enter the number of shifts you want to make: "))
    original_text = input("Enter the text: ").lower()

    if direction == "encode":
        encrypt(original_text, shift_amount)
    elif direction == "decode":
        decrypt(original_text, shift_amount)

    play_again = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if play_again != "yes":
        print("Goodbye!")
        break
