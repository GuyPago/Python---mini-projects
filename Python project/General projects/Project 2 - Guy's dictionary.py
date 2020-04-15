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
    user_input = str(input("Enter a value ('q' to quit or 'h' for help)\n")) or '0'
    if (user_input == "q"):
        print("\nClosing, Bye !")
        break
    elif (user_input == "h"):
        print("""\n'q' - Quit\n'h' - Help'\n'd' - Print full dictionary\n"""
              + "'l' - Print data size\n'a' - Add a new definition\n"
              + "'u' - Update extisting definiton\n\n")
    elif (user_input == '0'):
        print("\n\nNot entered any value\n")
    elif (user_input == 'd'):
        print('\nFull dictionary list\n')
        call_dictionary_list()
        print('\n')
    elif (user_input == 'l'):
        print("\nGuy's dictionary has a data base of",len(milon),"values.\n\n")
    elif (user_input == 'a'):
        new_key = str(input("\nEnter a new definiton:\n")).capitalize() or '0'
        new_value = str(input("\nEnter a value for '"+new_key+"':\n")).capitalize() or '0'
        if (new_key == '0') or (new_value == '0'):
            print("Error - not entered key/value.\n\n")
        elif (new_key in milon.keys()) or (new_value in milon.values()):
            print("\nError!\nDefinition already exists in dictionary.\nFor updating values enter 'u'\n")
    elif (user_input == 'u'):
        update_key = str(input("\nEnter existing definition\n")).capitalize() or '0'
        update_value = str(input("\nEnter a new value for ''"+update_key+"'\n")).capitalize() or '0'
        if (update_key == '0') or (update_value == '0'):
            print("Error!\nNot entered definition/value\n\n")
    else:
        search_key = user_input.capitalize()
        if search_key in milon.keys():
            value = milon[search_key]
            print("\nGuy's definiton for",user_input + ":\n" + user_input.capitalize(),'=',value + ".\n")
        else:
            print("Value doesn't exist, please select another value.\n")

milon["Sol"]
