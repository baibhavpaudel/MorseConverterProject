# Morse Code dictionary
morse_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.', '&': '.-...', "'": '.----.', '@': '.--.-.',
    ',': '--..--', '!': '-.-.--', '.': '.-.-.-', '-': '-....-', '?': '..--..', '"': '.-..-.',
    '/': '-..-.',
}

# Input
print("............WELCOME TO THE MORSE CODE CONVERTER!............")
text = input("............Text to convert into Morse Code: ").upper()
# Put every input character into a list
characters = [letter for letter in text.replace(" ", "")]

# Creates a list of codes after converting each character
morse_code = [morse_dict[char] for char in characters]

# Joins all the converted codes to form an output
converted_output = ''
for code in morse_code:
    converted_output += f" {code}"


print(f"The desired code is: ({converted_output})")
print("............SEE YOU AGAIN!............")




