
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


#  Multiplication table
x = 10
y = 10

for i in range(1, y+1):   # set a range of numbers | range('start','end','jump')
    for j in range(1, x+1):  # range always stops at (n-1). | range(0, n)
        print(i * j, "\t",end="")  # set a 'tab' spacing. | '\t'
    print()  # line break at the end of the loop.

# ^^^End^^^
