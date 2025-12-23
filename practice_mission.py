# first_script.py
# This is a comment. Python ignores it.
# The line below defines a function called 'main'
def main():
     # Everything indented under 'def main():' belongs to the function
    print("🎉 Welcome to your second Python script!")
    print("")  # This prints a blank line
    
     # Get user input and store it in a variable called 'favorite_color'
    favorite_color = input("What is your favorite color?")
     # Get user input and store it in a variable called 'favorite_number'
    favorite_number = input("What is your favorite number?")

    # An 'if/else' statement to check the input
    if favorite_color:  # This means "if favorite_color is not empty"
        # Lines indented here run only if the 'if' is True
        print(f"Hello, {favorite_color} is my favorite color, too! I also like {favorite_color}.")
        print(f"Your favorite color has {len(favorite_color)} letters in it.")
        try:
            number_as_int = int(favorite_number)
            if number_as_int > 10:
                print(f"Whoa, {number_as_int} is a big number!")
            else:
                print(f"{number_as_int} is a nice, modest number.")
        except ValueError:
            print("That doesn't look like a whole number. No problem!")
    else:
        # Lines indented here run only if the 'if' is False
        print("You didn't type a color. That's okay too!")

    print("")  # Another blank line
    print("This script is now finished. Well done!")

# This line is NOT indented, so it's NOT part of the function.
# It calls the 'main' function to start the program.
main()