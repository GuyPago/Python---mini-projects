# Guy's personal dictionary. Run code for instructions.

milon = {"Guy":"GuyPago",
         "Yulia":"Gezza",
         "Nir":"Betanir",
         "Ram":"Ateenim",
         "Sol":"Politis"}

def call_dictionary_list():
    for i,j in milon.items():
        print(i + ":",j)

print("Welcome to Guy's dictionary !\n")
while True:
    key_input = str(input("Enter a value ('q' to quit or 'h' for help)\n")) or '0'
    if (key_input == "q"):
        print("\nClosing, Bye !")
        break
    elif (key_input == "h"):
        print("""\n'q' - Quit\n'h' - Help'\n'd' - Print full dictionary\n"""
              + "'l' -Print data size\n\n")
    elif (key_input == 'd'):
        print('\nFull dictionary list\n')
        call_dictionary_list()
        print('\n')
    elif (key_input == 'l'):
        print("\nGuy's dictionary has a data base of",len(milon),"values.\n\n")
    elif (key_input == 'a'):
        new_key = str(input("Enter a new key:\n")).capitalize() or '0'
        new_value = str(input("Enter a definition for '"+new_key+"':\n")).capitalize() or '0'
        if (new_key == '0') or (new_value == '0'):
            print("Error - not entered key/value.\n\n")
        elif (new_key in milon.keys()) or (new_value in milon.values()):
            print("\nError!\nDefinition already exists in dictionary.\nFor updating values press 'u'\n")
    else:
        search_key = key_input.capitalize()
        if search_key in milon.keys():
            value = milon[search_key]
            print("\nGuy's definiton for",key_input + ":\n" + key_input.capitalize(),'=',value + ".\n")
        else:
            print("Value doesn't exist, please select another value.\n")
