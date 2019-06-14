from helpers import alphabet_position, rotate_character


def encrypt(text, rot):
    new_message = ''
    for letter in text:
        new_message += rotate_character(letter, rot)
    return new_message


def main():
    message = input("Type a message: \n")
    rotation = int(input('Rotate by: \n'))
    print(encrypt(message, rotation))


if __name__ == "__main__":
    main()
