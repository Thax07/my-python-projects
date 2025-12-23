# list_mission.py
def main():
    print("Let's make a list of your favorite foods!")
    print("")

    # 1. CREATE an empty list to store the foods
    favorite_foods = []  # Empty square brackets create an empty list

    # 2. USE A LOOP to ask for three foods
    # We'll ask 35 times. A 'for' loop can count for us.
    for i in range(5):  # range(5) gives us numbers 0, 1, 2, 3, 4
        # Ask for a food. (i+1) makes it ask for food 1, 2, 3 instead of 0, 1, 2.
        food = input(f"Enter favorite food {i+1}: ")
        # 3. APPEND the food to the list
        favorite_foods.append(food)

    print("")
    print("Alex's favorite foods are favorite foods are:")

    # 4. USE ANOTHER LOOP to print each food in the list
    for food in favorite_foods:  # For each item in the list...
        print(f"{food}!")   # ...print this line.

    print("")
    print("List mission complete!")

# Don't forget to call main()
main()