################################################################################
# nameProcessor.py
#  Spring 2022
# Author: Lily Zimmermann
#
# This program gets a string containing a person's first, middle, and last
# names and displays first, middle, and last initials.
################################################################################

################################################################################
# Main function that runs full program. This assigns values to the first, middle
# and last names.
################################################################################
def main():

    #declare variables
    round_number = 1

    #welcome user
    welcome_message()

    #request first, middle, and last name while checking for common
    #input errors like too many spaces or numbers
    first_name, round_number = name_validation(round_number)
    middle_name, round_number = name_validation(round_number)
    last_name, round_number = name_validation(round_number)

    #change first, middle, and last names to initials
    first_initial, middle_initial, last_initial = initial_return(first_name, middle_name, last_name)

    #print initials
    print(f"Your initials are:", first_initial, middle_initial,last_initial)

################################################################################
# This function contains a welcome message
################################################################################
def welcome_message():
    print("Welcome! I exist just to turn your name into initials. "
          "Let's get started!")

################################################################################
# This function requests a user for a name, validates if the user gave a name
# that only has letters, and returns the value to the main function.
################################################################################
def name_validation(round_number):

    #check which 'round' it is to see if it is user's first, etc. name
    if round_number == 1:
        name_type = "first"
    elif round_number == 2:
        name_type = "middle"
    elif round_number == 3:
        name_type = "last"
    else:
        print('Error name_validation')

    #request name from user
    print(f"What is your {name_type} name?")
    user_name = input(f"{name_type} name: ").upper()

    #validate if name only contains letters (no spaces, numbers, or other characters)
    while not user_name.isalpha():
        print(f"I'm sorry. Please only enter your {name_type} name.")
        user_name = input(f"{name_type} name: ")

    #return name entered
    round_number+=1
    return user_name, round_number

################################################################################
# This function takes in the names that were previously validated and returns
# what their initials would be.
################################################################################
def initial_return(first_name, middle_name, last_name):

    #change names into initials with a period after each
    first_initial = first_name[:1] + '.'
    middle_initial = middle_name[:1] + '.'
    last_initial = last_name[:1] + '.'

    #return initials
    return first_initial, middle_initial, last_initial

# Execute the main function
if __name__ == '__main__':
    main()
