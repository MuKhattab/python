alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    cyphar_text=''
    for i in text:
        orginal_alpha_index=alphabet.index(i)
        cyphar_index=orginal_alpha_index + shift
        if (cyphar_index > 26):
            cyphar_index -=26
        cyphar_text+=alphabet[cyphar_index]
    print(f"the ecrypted text for: {text} is {cyphar_text}")


def decrypt(cyphar, shift):
    decrypt_text=''
    for i in cyphar:
        position=alphabet.index(i)
        cyphar_index = position + shift
        if (cyphar_index > 26):
            cyphar_index -= 26
        cyphar_text += alphabet[cyphar_index]
    print(f"the ecrypted text for: {text} is {cyphar_text}")


def ceaser (ceaser_type, text, shift):
    converted_text=''
    if ceaser_type == "encode":
        for i in text:
            if i in alphabet:
                position = alphabet.index(i)
                cyphar_index = position + shift
                cyphar_index= cyphar_index % 26
                converted_text += alphabet[cyphar_index]
            else:
                converted_text+= i
        print(f"the decrypted text of: {text} is {converted_text}")
    elif ceaser_type == "decode":
        for i in text:
            if i in alphabet:
                position = alphabet.index(i)
                cyphar_index = position - shift
                cyphar_index = cyphar_index % 26
                converted_text += alphabet[cyphar_index]
            else:
                converted_text += i
        print(f"the decrypted text of: {text} is {converted_text}")




again = "y"
while (again=="y"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(direction, text, shift)

    again=input("Do you want to run again? y/n:")
if again=="n":
    print("Good Bye")
