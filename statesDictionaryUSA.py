##############################################################################
# statesDictionaryUSA.py
# Spring 2022
# Author: Lily Zimmermann
###############################################################################
# This program creates a dictionary containing the U.S. states as keys and their
# capitals as values. The program will randomly quiz the user by displaying the
# name of a state and ask the user to enter that state's capital. The program
# keeps a count of the number of correct and incorrect responses.
###############################################################################
import random

################################################################################
# This is the main function that executes all code of the program
################################################################################
def main():

    # Welcome the user
    welcome()

    # Create dictionary with U.S. states & their capitals
    states_and_capitals = set_up_states()

    # Quizz user
    correct_answers,incorrect_answers = quiz_user(states_and_capitals)

    # Give the number of correct and incorrect answers to the user
    results(correct_answers,incorrect_answers)

################################################################################
# This function contains a welcome message
################################################################################
def welcome():
    print("Time to Study!\n"
          "I'm going to test you on your ability to remember U.S. States.\n"
          "Are you ready? Great! Let's go!")

################################################################################
# This function creates a dictionary containing the U.S. states & their capitals
################################################################################
def set_up_states():
    states_and_capitals = {'ALABAMA': 'MONTGOMER', 'ALASKA': 'JUNEAU', 'ARIZONA': 'PHOENIX',
                           'ARKANSAS': 'LITTLE ROCK', 'CALIFORNIA': 'SACRAMENTO',
                           'COLORADO': 'DENVER', 'CONNECTICUT': 'HARTFORD', 'DELAWARE': 'DOVER',
                           'FLORIDA': 'TALLAHASSEE', 'GEORGIA': 'ATLANTA', 'HAWAII': 'HONOLULU',
                           'IDAHO': 'BOISE', 'ILLINOIS': 'SPRINGFIELD', 'INDIANA': 'INDIANAPOLIS',
                           'IOWA': 'DES MOINES', 'KANSAS': 'TOPEKA', 'KENTUCKY': 'FRANKFORT',
                           'LOUISIANA': 'BATON ROUGE', 'MAINE': 'AUGUSTA', 'MARYLAND': 'ANNAPOLIS',
                           'MASSACHUSETTS': 'BOSTON', 'MICHIGAN': 'LANSING', 'MINNESOTA': 'SAINT PAUL',
                           'MISSISSIPPI': 'JACKSON', 'MISSOURI': 'JEFFERSON CITY', 'MONTANA': 'HELENA',
                           'NEBRASKA': 'LINCOLN', 'NEVADA': 'CARSON CITY', 'NEW HAMPSHIRE': 'CONCORD',
                           'NEW JERSEY': 'TRENTON', 'NEW MEXICO': 'SANTA FE', 'NEW YORK': 'ALBANY',
                           'NORTH CAROLINA': 'RALEIGH', 'NORTH DAKOTA': 'BISMARCK', 'OHIO': 'COLUMBUS',
                           'OKLAHOMA': 'OKLAHOMA CITY', 'OREGON': 'SALEM', 'PENNSYLVANIA': 'HARRISBURG',
                           'RHODE ISLAND': 'PROVIDENCE', 'SOUTH CAROLINA': 'COLUMBIA', 'SOUTH DAKOTA': 'PIERRE',
                           'TENNESSEE': 'NASHVILLE', 'TEXAS': 'AUSTIN', 'UTAH': 'SALT LAKE CITY',
                           'VERMONT': 'MONTPELIER', 'VIRGINIA': 'RICHMOND', 'WASHINGTON': 'OLYMPIA',
                           'WEST VIRGINIA': 'CHARLESTON', 'WISCONSIN': 'MADISON', 'WYOMING': 'CHEYENNE'}

    # Return the dictionary containing U.S. states & their capitals to the main function
    return states_and_capitals

################################################################################
# This function quizzes the user on all the states and their capitals
################################################################################
def quiz_user(states_and_capitals):

    #Create variables to tally user's score
    correct_answers = 0
    incorrect_answers = 0
    testing_user = "true"

    while testing_user == "true":
        # Choose a random state from the states_and_capitals dictionary
        random_state = random.choice(list(states_and_capitals))

        # Copy the random state and its value to a new dictionary called temp_quiz
        temp_quiz = {random_state: states_and_capitals[random_state]}

        # Remove the random state from the states_and_capitals dictionary
        del states_and_capitals[random_state]

        # Ask the user for the capital of the randomly selected state
        # Remove any spaces and capitalize all letters to make the user answer
        # and temp_quiz dictionary match
        print(f"\nWhat is the capital of {random_state}?")
        user_answer = input(f"Capital of {random_state}: ").upper().replace(" ", "")

        # Tell user if answer was correct. Tally incorrect and correct answers
        if user_answer == temp_quiz[random_state].upper().replace(" ", ""):
            print(f"\nGreat job! You are correct." +
                  f"The capital of {random_state} is {temp_quiz[random_state]}.\n")
            correct_answers += 1
        else:
            print(f"\nI'm sorry. That is not correct.\n"
                  f"The capital of {random_state} is {temp_quiz[random_state]}.\n")
            incorrect_answers += 1

        # Check if there are any states left in the states_and_capitals dictionary
        # No states left = return the user's score
        # States remaining = continue with quiz_user function
        if len(states_and_capitals) == 0:
            print("Congrats! You reviewed all the U.S. States!")
            return correct_answers, incorrect_answers

        # Ask if user wants to continue quizzing
        # Yes = continue with quiz_user function
        # No = return user's score to the main function
        received_valid_input = 'N'

        while received_valid_input == 'N':
            print(f"Do you want to continue?\n"
                f"1 = Yes\n"
                f"2 = No")
            still_quizzing = input("Continue?: ")

            if still_quizzing == '1':
                    received_valid_input = 'Y'
            elif still_quizzing == '2':
                return correct_answers, incorrect_answers
            else:
                print(f"I'm sorry. I don't understand.\n")

################################################################################
# This function tells the user their results
################################################################################
def results(correct_answers,incorrect_answers):
    print(f"\nNumber of Correct Answers: {correct_answers}\n"
          f"Number of Incorrect Answers: {incorrect_answers}")
    final_grade_percentage = round(((correct_answers*100)/(correct_answers+incorrect_answers)), 1)
    print(f"That means you answered {final_grade_percentage} % of the questions correctly.")

    # Go to the final function in the program
    final_message(final_grade_percentage)

################################################################################
# This function gives a final message depending on the user's % of correct answers
################################################################################
def final_message(final_grade_percentage):
    if final_grade_percentage >= 90:
        print("You did an amazing job!")
    elif final_grade_percentage < 90 and final_grade_percentage >= 80:
        print("You did a good job!")
    elif final_grade_percentage < 80 and final_grade_percentage >= 70:
        print("You didn't do terribly, but you might want to study more.")
    elif final_grade_percentage < 70 and final_grade_percentage >= 60:
        print("I'd suggest studying a bit more.")
    elif final_grade_percentage < 60 and final_grade_percentage >= 50:
        print("I would suggest getting a tutor.")
    elif final_grade_percentage < 50 and final_grade_percentage >= 0:
        print("Uh oh!")
    else:
        print("Final message error")

    print(f"\nFeel free to return any time you need to study your state capitals.")

# Execute the main function
if __name__ == '__main__':
    main()
