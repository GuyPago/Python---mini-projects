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
    user_input = str(input("Enter a value to search "
                     + "('q' to quit or 'h' for help)\n")) or '0'
    if (user_input == "q"):
        print("\nThanks for using Guy's dictionary, Bye !")
        break
    elif (user_input == "h"):
        print("\n\nDictionary RoadMap:\n'q' - Quit\n'h' - Help\n'd' - Print full dictionary\n"
              + "'l' - Print data size\n'a' - Add a new definition\n"
              + "'u' - Update extisting value\n'r' - Remove extisting definiton\n")
    elif (user_input == '0'):
        print("\n\nNot entered any value\n")
    elif (user_input == 'd'):
        print('\nFull dictionary list\n')
        call_dictionary_list()
        print('\n')
    elif (user_input == 'l'):
        print("\nGuy's dictionary has a data base of",len(milon),"values.\n\n")
    elif (user_input == 'a'):
        new_key = str(input("\nEnter a new value:\n")).capitalize() or '0'
        new_value = str(input("\nEnter a value for '"+new_key+"':\n")).capitalize() or '0'
        if (new_key == '0') or (new_value == '0'):
            print("Error - not entered key/value.\n\n")
        elif (new_key in milon.keys()) or (new_value in milon.values()):
            print("\nError!\nDefinition already exists in dictionary.\nFor updating values enter 'u'\n")
        else:
            milon[new_key] = new_value
            print("\nSuccess!\nAdded '" + new_key+"' to dictionary\n\n")
    elif (user_input == 'u'):
        update_key = str(input("\nEnter existing value:\n")).capitalize() or '0'
        if (update_key not in milon.keys()):
            print("\ncan't update '" + update_key +
                  "' because it doesn't exist.\nFor adding new values, enter 'a'\n\n")
        else:
            update_value = str(input("\nEnter a new value for '"+update_key+"':\n")).capitalize() or '0'
            if (update_key == '0') or (update_value == '0'):
                print("Error!\nNot entered definition/value\n\n")
            else:
                milon.update({update_key:update_value})
                print("\nSuccess!\nUpdated '" + update_key+"' in dictionary\n\n")
    elif (user_input == 'r'):
        remove_key = str(input("\nEnter value to remove:\n")).capitalize() or '0'
        if (remove_key not in milon.keys()):
            print("\nError!\n'" + remove_key + "' doesn't exist.\n\n")
        else:
            r_conf = str(input("\nAre you sure you want to remove '"+remove_key
                         + "' from dictionary? ('y' - Yes)\n")) or '0'
            if (r_conf == 'y'):
                milon.pop(remove_key)
                print("\nSuccess!\n'" + remove_key +
                      "' has been removed from dictionary\n\n")
            else:
                print("Operation cancelled\n\n")
                pass
    else:
        search_key = user_input.capitalize()
        if search_key in milon.keys():
            value = milon[search_key]
            print("\nGuy's definiton for",user_input + ":\n" + user_input.capitalize(),'=',value + ".\n")
        else:
            print("\n'" + search_key + "' doesn't exist, please select another value.\n\n")
