'''
    Israel Ayala
    03/09/2023
    Main application uses the hierarchy from classroom, menu options
    from menu.py and the linked list from arr_list.py. We use an array
    from numpy and the implemeneted linked list to create an array of size
    3 where each index is a classroom type with a linked list to add numerous
    classes.
'''
from menu import *
from classroom import *
from arr_list import *
from bst import *
import numpy as np

def main():
    # Create an array of size 3 with empty objects
    classrooms = np.empty(3, dtype=object)

    # Create a BST
    course_schedule = bst()

    # Create a linked_list() in each index of array
    for i in range(3):
        classrooms[i] = linked_list()

    print("\nWelcome to Classroom Manager!")

    done = False
    while not done:
        print("\nWhat would you like to do?")
        manage = manager()
        if manage == 1:
            option = room_options()
            # 1: Add a new classroom
            if option == 1:
                select = room_types()
                # Add a computer lab room
                if select == 1:
                    # Computer lab room object
                    lab_room = lab("","","")
                    # Read in info
                    lab_room.read()
                    # Insert to linked list at correct index
                    classrooms[0].insert(lab_room)
                # Add a projector room
                if select == 2:
                    # Projector room object
                    proj_room = projector("","","")
                    # Read in info
                    proj_room.read()
                    # Insert to linked list at correct index
                    classrooms[1].insert(proj_room)
                # Add a zoom room
                if select == 3:
                    # Zoom room object
                    zoom_room = zoom("","","")
                    # Read in info
                    zoom_room.read()
                    # Insert to linked list at correct index
                    classrooms[2].insert(zoom_room)

            # 2: Display which classroom?
            if option == 2:
                select = room_types()
                if select == 1:
                    classrooms[0].display()
                if select == 2:
                    classrooms[1].display()
                if select == 3:
                    classrooms[2].display()

            # 3: Removes the last classroom entered from given index
            if option == 3:
                select = room_types()
                if select == 1:
                    classrooms[0].delete()
                if select == 2:
                    classrooms[1].delete()
                if select == 3:
                    classrooms[2].delete()

        # Program 5, work with course schedule
        if manage == 2:
            option = course_options()
            # Add a course
            if option == 1:
                select = courses()
                # Add CS161
                if select == 1:
                    cs161 = course("","","")
                    cs161.set_course("CS161")
                    cs161.read()
                    course_schedule.insert(cs161)
                # Add CS162
                if select == 2:
                    cs162 = course("","","")
                    cs162.set_course("CS162")
                    cs162.read()
                    course_schedule.insert(cs162)
                # Add CS163
                if select == 3:
                    cs163 = course("","","")
                    cs163.set_course("CS163")
                    cs163.read()
                    course_schedule.insert(cs163)

            # Display all courses
            if option == 2:
                course_schedule.display()

            # Display by a given type
            if option == 3:
                select = courses()
                if select == 1:
                    course_schedule.display_type("CS161")
                if select == 2:
                    course_schedule.display_type("CS162")
                if select == 3:
                   course_schedule.display_type("CS163")

             # Remove a course # Not working!
            if option == 4:
                select = courses()
                if select == 1:
                    course_schedule.remove("CS161")
                if select == 2:
                    course_schedule.remove("CS162")
                if select == 3:
                   course_schedule.remove("CS163")

        # Quit
        if manage == 3:
            done = True

if __name__ == "__main__":
    main()