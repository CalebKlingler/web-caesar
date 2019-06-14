def alphabet_position(letter):
    letter = letter.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.find(letter)


def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_char = char
    if char.isalpha():
        new_position = (alphabet_position(char) + rot) % 26
        new_char = alphabet[new_position]
        if char.isupper():
            new_char = new_char.upper()
    return new_char
