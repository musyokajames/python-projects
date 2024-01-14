#Caesar Cypher.This is going to be fun :)

#Create a dictionary
caesar_mapping = {
    "A": "D",
    "B": "E",
    "C": "F",
    "D": "G",
    "E": "H",
    "F": "I",
    "G": "J",
    "H": "K",
    "I": "L",
    "J": "M",
    "K": "N",
    "L": "O",
    "M": "P",
    "N": "Q",
    "O": "R",
    "P": "S",
    "Q": "T",
    "R": "U",
    "S": "V",
    "T": "W",
    "U": "X",
    "V": "Y",
    "W": "Z",
    "X": "A",
    "Y": "B",
    "Z": "C",
}

reverse_caesar = {normal_character : caesar_character for caesar_character,normal_character in caesar_mapping.items()}

def encrypt(text):
    text = text.upper()

    caesar_string = ""

    for char in text:
        if char == " ":
            caesar_string += ""
        else:
            caesar_string += caesar_mapping.get(char,"?")
    return caesar_string

def decrypt(text):
    text=text.upper()

    normal_string = ""

    for char in text:
        if char ==" ":
            normal_string += ""
        else:
            normal_string += reverse_caesar.get(char,"?")
    return normal_string

prompt = '''What do you want to do?
A)Encrypt
B)Decrypt
'''
print(prompt)
while True:
    user_choice = input("Enter your Choice(A/B):")
    if user_choice.upper() in {"A","B"}:
        user_input = input("Enter the statement:")
        if user_choice.upper() == "A":
             print(encrypt(user_input))
        elif user_choice.upper() == "B":
            print(decrypt(user_input))
        break
    else:
        print("Please enter a valid choice.A or B")
   
   
