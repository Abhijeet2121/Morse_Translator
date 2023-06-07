# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(message):
    cipher = ""
    for letter in message:
        if letter != " ":
            # Looks up the dictionary and adds the corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + " "
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += " "
    return cipher

def decrypt(message):
    # extra space added at the end to access the last morse code
    message += " "
    citext = ""
    decipher = ""

    for letter in message:
        if letter != " ":
            #keeps track of spaces
            i = 0
            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
            # if i = 2 that indicates a new word
            if i == 2:
                # adding space to separate words
                decipher += " "
            else:
            # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ""
    return decipher

user_input = input("Enter any text you want to convert: ")
result = encrypt(user_input.upper())
print(f"Morse code of {user_input}: {result}")

morse_code_to_convert = input("Enter any Morse code to decode: ")
output = decrypt(morse_code_to_convert)
print(f"Word of Morse code {morse_code_to_convert}: {output}")