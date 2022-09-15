# list_of_numbers.py
# Spring 2022
# Author: Lily Zimmermann
#
# This program prompts a user to enter a series of 20 numbers
# Numbers will be stored in a list. The min, max, and average
# of the numbers will be printed along with the total number
# of elements in the list.

def main():
    # creating a list to hold 20 numbers & creating variable to note
    # the length of the list
    user_numbers = [None] * 20

    # asking for user input for list
    print('Enter 20 numbers please: ')

    for index in range(len(user_numbers)):
        user_numbers[index] = float(input())

    # calculating total of all values entered by user
    total = 0.0
    for index in user_numbers:
        total += index

    # calculating average of all values entered by user
    average = total / len(user_numbers)

    # printing information about the group of numbers entered by the user
    print('The number you entered with the lowest value is:', min(user_numbers))
    print('The number you entered with the highest value is:', max(user_numbers))
    print('The total of the numbers you entered was: ', total)
    print('The average of the numbers you entered is', average)


# call the main function
if __name__ == '__main__':
    main()
