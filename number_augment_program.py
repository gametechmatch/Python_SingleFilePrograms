########################################################################
# number_augment_program.py
# Author: Lily Zimmermann
# Spring 2022
########################################################################
# This program uses recursion to count from 1 to a number entered by the
# user
########################################################################
# This is the main function that handles all code
def main():
    # Ask user for a value greater than 1
    waiting_for_valid_input = True
    while waiting_for_valid_input:
        user_input = input("Please enter an integer greater than 1: ")
        if user_input.isdigit():
            if int(user_input) > 1:
                waiting_for_valid_input = False

    # Run the user input and a counter through the number_augment
    # function until all values up to the user entered number have
    # been printed
    num = int(user_input)
    counter = 1
    number_augment(num, counter)

# This function prints a value up to the number entered by the user
def number_augment(num, counter):
    if counter < (num +1):
        print(counter)
        counter = counter + 1
        number_augment(num, counter)

#Execute main program
if __name__ == '__main__':
    main()
