##############################################################################
# course_dictionary.py
# Spring 2022
# Lily Zimmermann
###############################################################################
# This program asks a user for a course that they are taking and then prints
# out the corresponding room, instructor, and times for the selected course.
##############################################################################

def main():

    # Create the dictionaries holding courses and their corresponding room numbers,
    # instructors, and times
    uni_course_rooms = {'CS101':'3004', 'CS102':'4501','CS103':'6755','NT110':'1244',
               'CM241':'1411'}
    uni_course_instructors = {'CS101':'Haynes', 'CS102':'Alvarado','CS103':'Rich',
                          'NT110':'Burke', 'CM241':'Lee'}
    uni_course_times = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.','CS103':'10:00 a.m.',
                          'NT110':'11:00 a.m.', 'CM241':'1:00 p.m.'}

    # Request course from user
    # Capitalize the input and remove spaces to match the dictionary options
    print('What course would you like to look up?')
    course = input('Course: ').replace(" ","").upper()

    # Check if user input for the course is one of the courses to pick from
    while course not in uni_course_rooms:
        print("\nI'm sorry. I cannot find that course. "
              "These are the courses you can choose from:")
        print('CS101, CS102, CS103, NT110, or CM241\n')
        print('What course would you like to look up?')
        course = input('Course: ').replace(" ","").upper()

    # Print out corresponding room, instructor, and times for the applicable course
    print(f'{course} room: {uni_course_rooms[course]}')
    print(f'{course} instructor: {uni_course_instructors[course]}')
    print(f'{course} time: {uni_course_times[course]}')

# Execute the main function
if __name__ == '__main__':
    main()
