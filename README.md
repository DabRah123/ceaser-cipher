# Caesar Cipher CLI Tool
This is a simple Caesar Cipher implementation in Python. The tool allows you to encode and decode text using a specified shift amount. It features a CLI (Command Line Interface) that repeatedly prompts users to encrypt or decrypt text.

## Features
Encryption: Converts plain text into encoded text using a shift in the alphabet.
Decryption: Converts encoded text back to plain text by reversing the shift.
ASCII Art: Displays a banner for the program for better user experience.
Input Validation: Ensures users enter valid inputs for options and numbers.

## Files
ascii_art.py
Contains the ASCII art banner displayed when the program starts.

main.py
Contains the main logic for encrypting and decrypting text using the Caesar Cipher algorithm.

## How It Works
The Caesar Cipher shifts each letter of the input text by a specified number of places in the alphabet. Non-alphabetic characters remain unchanged.

## Example:

Plain text: hello
Shift: 2
Encoded text: jgnnq

## Prerequisites
Python 3.7 or later

## Algorithm
The program follows these steps:

## Encryption Algorithm
Take the plain text and shift amount as inputs.
For each character in the text:
If it is a lowercase letter:
Find its position in the alphabet (0-indexed).
Add the shift amount and use modulus (%) with 26 to handle wrapping.
Replace the character with the new shifted letter.
If it is not a letter, keep it unchanged.
Combine the modified characters into the encoded text.
Display the encoded text.

## Decryption Algorithm
Take the encoded text and shift amount as inputs.
For each character in the text:
If it is a lowercase letter:
Find its position in the alphabet (0-indexed).
Subtract the shift amount and use modulus (%) with 26 to handle wrapping.
Replace the character with the new shifted letter.
If it is not a letter, keep it unchanged.
Combine the modified characters into the decoded text.
Display the decoded text.

## Main Program Flow
Display the ASCII art from ascii_art.py.
Ask the user if they want to encode or decode.
Validate the user’s input for the shift amount and text.
Call the respective function (encrypt or decrypt) based on the user’s choice.
Prompt the user to continue or exit.
If the user exits, display a goodbye message and terminate the program.
