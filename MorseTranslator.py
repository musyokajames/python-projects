#Morse code translator

#Create a dictionary that maps alphabets to morse code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.'
}
#creating a dictionary for reverse maping
reverse_mapping = {character:morse_value for morse_value,character in morse_code_dict.items()}

#Create a function that handle the translation
def translate_to_morse(text):
    #handle the case-issue,let all the input be changed to a specific case
    text = text.upper()

    #initialise an empty morse code string
    morse_string = ""

    #create a loop that goes through all the characters in the input and translates each individual character to the respective mapping on the morse code dictionary
    for char in text:
            try:
                if char == " ":
                    morse_string += "  "
                else:
                    morse_string += morse_code_dict[char] + ""
            except KeyError :
                 print("Sorry, I can't translate this character(s):",char)
                 morse_string += char + ""             
    return morse_string


def translate_from_morse(morse_code):
    
    #split the morse code into individual characters
    morse_characters = morse_code.split(" ")

    #initialise a normal statement
    english_string = ""
    for morse_char in morse_characters:
        if morse_char == " ":
            english_string += " "
        else:
            english_string += reverse_mapping.get(morse_char,"?")
    return english_string

#Get the user's input
#first the user must choose what kind of translation they want to do
#here i used multiline strings (""""")
#through-out the code i use .upper() so that the input is changed to uppercase to make it easy
prompt = '''What translation do you want to do?
A)English to Morse
B)Morse to English
'''
print(prompt)
while True:
    user_choice = input("Enter your choice(A/B):")
    if user_choice.upper() in {"A","B"}:
        user_input = input("Enter your statement:")
        if user_choice.upper() == "A":
            print(translate_to_morse(user_input))
        elif user_choice.upper() == "B":
            print(translate_from_morse(user_input))
        break
    else:
        print("Invalid input.Enter either A or B")



