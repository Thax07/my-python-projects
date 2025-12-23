# practice_mission.py
# This is a comment. Python ignores it.
# The line below defines a function called 'main'
def main():
    # Everything indented under 'def main():' belongs to the function
    print("🎉 Welcome to your second Python script!")
    print("")  # This prints a blank line

    # Get user input and store it in a variable called 'favorite_color'
    favorite_color = input("What is your favorite color? ")
    # CHANGED: Use a NEW variable 'favorite_number' to store the second answer
    favorite_number = input("What is your favorite number? ")

    # An 'if/else' statement to check the input
    if favorite_color:  # This means "if favorite_color is not empty"
        # Lines indented here run only if the 'if' is True
        # CHANGED: Use both variables in the message. Also fixed f-string syntax.
        print(f"Wow, {favorite_color} is a great color!")
        print(f"And {favorite_number} is an interesting number.")
        # CHANGED: len() uses parentheses (), not curly braces {}.
        print(f"Your color's name has {len(favorite_color)} letters in it.")
    else:
        # Lines indented here run only if the 'if' is False
        # CHANGED: Updated the message to be about the color.
        print("You didn't type a color. That's okay too!")

    print("")  # Another blank line
    # BONUS MISSION: Add an if statement for the number here.
    print("This script is now finished. Well done!")

# This line is NOT indented, so it's NOT part of the function.
# It calls the 'main' function to start the program.
main()