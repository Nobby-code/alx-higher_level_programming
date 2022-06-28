#!/usr/bin/python3
def uppercase(str):
    for character in str:
        temp = ord(character)
        if temp > 96 and temp < 123:
            character = chr(temp - 32)
        print("{}".format(character), end="")
    print("")
