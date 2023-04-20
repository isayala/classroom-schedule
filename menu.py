'''
    Israel Ayala
    03/15/2023
    CS302
    menu.py is used to structure functions only designed for the menu
    This makes main have less code 
''' 

# Select options for program 4 or 5
def manager():
    valid_option = False
    while not valid_option:
        print("\n1: Work with classrooms",
              "\n2: Work with course schedule",
              "\n3: Quit")
        select = int(input("\nPlease make a selection: "))
        if select < 1 or select > 3:
            print("\nNot a valid selection. Please try again!")
        else:
            valid_option = True
        return select

# Display what user wants to do
def room_options():
    valid_option = False
    while not valid_option:
        print("\n1: Add a new classroom", # Program 4
              "\n2: Display a classroom",
              "\n3: Remove a classroom")
        select = int(input("\nPlease make a selection: "))
        if select < 1 or select > 3:
            print("\nNot a valid selection. Please try again!")
        else:
            valid_option = True

    return select

# Display types of classrooms
def room_types():
    valid_option = False
    print("\nHere are your choices for classrooms.")
    while not valid_option:
        print("\n1: Computer Lab Room",
              "\n2: Projector Room",
              "\n3: Zoom Room")
        select = int(input("\nPlease make a selection: "))
        if select < 1 or select > 3:
            print("\nNot a valid selection. Please try again!")
        else:
            valid_option = True

    return select

# Display the options we have for course manager
def course_options():
    valid_option = False
    print("\nHere are your choices for the schedule.")
    while not valid_option:
        print("\n1: Add a course", 
              "\n2: Display your courses",
              "\n3: Display by a given type",
              "\n4: Remove a course")
        select = int(input("\nPlease make a selection: "))
        if select < 1 or select > 4:
            print("\nNot a valid selection. Please try again!")
        else:
            valid_option = True

    return select 

# List types of courses
def courses():
    valid_option = False
    print("\nList of courses available.")
    while not valid_option:
        print("\n1: CS161",
              "\n2: CS162", 
              "\n3: CS163")
        select = int(input("\nPlease make a selection: "))
        if select < 1 or select > 3:
            print("\nNot a valid selection. Please try again!")
        else:
            valid_option = True
        
    return select

# List times available
def timing():
    valid_option = False
    print("\nList of times available for this course.")
    while not valid_option:
        print("\n1: 09:00 AM",
              "\n2: 10:00 AM",
              "\n3: 11:00 AM",
              "\n4: 12:00 PM",
              "\n5: 01:00 PM",
              "\n6: 02:00 PM",
              "\n7: 03:00 PM",
              "\n8: 04:00 PM",
              "\n9: 05:00 PM")
        select = int(input("\nPlease make a selection: "))
        if select < 1 or select > 9:
            print("\nNot a valid selection. Please try again!")
        else:
            valid_option = True

    return select

# Display the days available
def days(): 
    valid_option = False
    while not valid_option:
        print("\n1: Monday/Wednesday",
              "\n2: Tuesday/Thursday",
              "\n3: Wednesday/Friday")
        select = int(input("\nPlease make a selection: "))
        if select < 1 or select > 3:
            print("\nNot a valid selection.")
        else:
            valid_option = True
            
    return select