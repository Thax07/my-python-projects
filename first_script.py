# first_script.py
# This is a comment. Python ignores it.
# The line below defines a function called 'main'
def main():
    # Everything indented under 'def main():' belongs to the function
    print("🎉 Welcome to your first Python script!")
    print("")  # This prints a blank line

    # Get user input and store it in a variable called 'user_name'
    user_name = input("What is your name? ")

    # An 'if/else' statement to check the input
    if user_name:  # This means "if user_name is not empty"
        # Lines indented here run only if the 'if' is True
        print(f"Hello, {user_name}! Great to have you here.")
        print(f"Your name has {len(user_name}} letters in it.")
    else:
        # Lines indented here run only if the 'if' is False
        print("You didn't type a name. That's okay too!")

    print("")  # Another blank line
    print("This script is now finished. Well done!")

# This line is NOT indented, so it's NOT part of the function.
# It calls the 'main' function to start the program.
main()