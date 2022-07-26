#!/usr/bin/python3

""" String Indentation Function """


def text_indentation(text):

    """
    def text_indentation(text):
        Args:
            text (must be a str type)
        If the string char in [".", "?", ":"]:
            adds new 2 lines after the character
        Raises:
            TypeError("must be a tring") if text !str
        Prints:
            the stripped string
    """
    new_character = ""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in text:
        new_character += char
        if char == "." or char == "?" or char == ":":
            # you can use if char in[".", "?", ":"]:
            new_character = new_character + "\n\n"
            print(new_character.strip() + "\n")
            new_character = ""

    print(new_character.strip(), end="")
