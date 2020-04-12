
# Convert user input to 'ASCII' language.
while True:
    user_input = input("enter any key to print(enter 'q' to quit):\n") or "0"  # '0' is default input.
    if user_input == "q":
        print("ending program...bye!\n\n\n")
        break  # Break/end the loop.
    else:
        print("user input was",user_input)
        print("the value of",user_input,"in ASCII is",str(ord(user_input)),"\n\n\n")

# ^^^End^^^
