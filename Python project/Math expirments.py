import math
import random
math.sqrt(2)

Guy = "me"

milon = {"guy":"Gezza(boy)","yulia":"Gezza(girl)","nir":"Betanir"}

def call_dictionary_list():
    for i,j in milon.items():
        print(i + ":",j)

print("Welcome to Guy's dictionary !\n")
while True:
    key_input = str(input("Enter a value ('q' to quit or 'h' for help)\n")) or 0
    if (key_input == "q"):
        print("\nClosing, Bye !")
        break
    elif (key_input == "h"):
        print("\n'q' - Quit\n'h' - Help'\n'd' - Print full dictionary\n")
    elif (key_input == 'd'):
        print('\n')
        call_dictionary_list()
        print('\n')
    else:
        value = milon[key_input.lower()]
        print("\n" + key_input.capitalize(),'=',value + ".\n")
