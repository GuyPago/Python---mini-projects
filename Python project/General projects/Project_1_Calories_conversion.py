# """Guy's self-made calories conversion algorithm.

def calory_from_100g(food_weight=0,calories_for_100grams=0):

    if (food_weight == 0) or (calories_for_100grams == 0):
        return "Not entered calories/food weight.\n\n"
    calories = calories_for_100grams / 100 * food_weight
    return calories

while True:
    calory_input = input("Enter calories for 100 grams (enter 'q' to quit)\n") or 0
    if (calory_input == 'q'):
        print("\nClosing, Bye !")
        break
    else:
        pass
    weight_input = input("Enter food weight (grams)\n") or 0
    answer = calory_from_100g(float(weight_input),float(calory_input))
    if (calory_input == 0) or (weight_input == 0):
        print(answer)
    else:
        print("\n\nYour food has:\n",answer,"calories for",weight_input,"grams\n\n")
