'''
    Israel Ayala
    03/09/2023
    Structures a hierarchy with classroom being the base class.
    The base class is a classroom with a room number, number of seats, and 
    a type of classroom. Then we have three derived classes, labroom,
    projector room, and zoom room (equipped with tech for zoom lectures).
'''
import os
from menu import *

# This hierarchy is mainly used in Program 4
# Base class room structures the room number, the type of room, and zoom
class room:
    # Constructor
    def __init__(self):
            # Classroom number
            self._room = ""
            # Type of classroom
            self._type = ""
            # Number of seats
            self._seats = ""

    # Constructor with arguments
    def __init__(self, room, type, seats):
        self._room = room
        self._type = type
        self._seats = seats

    # Destructor
    def __del__(self):
        self._room = ""
        self._type = ""
        self._seats = ""

    # Overload +
    # Add more seats if they become available
    def __add__(self, other):
        new_seats = self._seats + other._seats
        return new_seats

    # Overload +=
    def __iadd__(self, other):
        self._seats = self._seats + other._seats
        return self

    # Read in data without the classtype
    def read(self):
        # Grab the classroom number
        done = False
        while not done:
            temp = input("\nPlease enter the classroom number: ")
            try:
                self._room = int(temp)
                done = True
            except ValueError:
                print("Not an integer. Please try again!")
        
        # And the number of seats available...
        done = False
        while not done:
            temp = input("How many number of seats are available in the classroom: ")
            try: 
                self._seats = int(temp)
                done = True
            except ValueError:
                print("Not an integer. Please try again!")

    # Display
    def display(self):
        print("\nClassroom Number:", self._room, "\nClass Type: " + self._type, 
              "\nSeats available:", self._seats)

    # Set the type of room this is
    def set_type(self, type):
        self._type = type

    # Get the type of room
    def get_type(self):
        return self._type

    # Return the room number
    def get_room(self):
        return self._room
    
    # Return the number of seats
    def get_seats(self):
        return self._seats

# Computer-lab room, has computers, monitors
class lab(room):
    # Constructor
    def __init__(self):
        # Number of computers
        self._computers = ""
        # Number of monitors
        self._monitors = ""
        # Number of outlets
        self._outlets = ""

    # Constructor with arguments
    def __init__(self, computers, monitors, outlets):
        self._computers = computers
        self._monitors = monitors
        self._outlets = outlets

    # Add a new computer-lab classroom
    def read(self):
        super().read()
        super().set_type("Computer Lab Room")
        done = False
        while not done:
            temp = input("\nEnter the amount of computers available: ")
            try:
                self._computers = int(temp)
                done = True
            except ValueError:
                print("\nNot an integer. Please try again!")

        done = False
        while not done:
            temp = input("Enter the amount of monitors available: ")
            try:
                self._monitors = int(temp)
                done = True
            except ValueError:
                print("\nNot an integer. Please try again!")

        done = False
        while not done:
            temp = input("Enter the amount of outlets available: ")
            try:
                self._outlets = int(temp)
                done = True
            except ValueError:
                print("\nNot an integer. Please try again!")

    # Use super display as well
    def display(self):
        super().display()
        print("\nComputers available:", self._computers, "\nMonitors Available:",
              self._monitors, "\nOutlets available:", self._outlets)

# Projector room has a light source, a screen, and distance
class projector(room):
    # Constructor 
    def __init__(self):
        # Projector light source
        self._light = ""
        # Screen width
        self._width = ""
        # Distance between the projector and the screen
        self._distance = ""

    # Constructor with arguments
    def __init__(self, light, width, distance):
        self._light = light
        self._width = width
        self._distance = distance

    # Add in a new projector classroom
    def read(self):
        super().read()
        super().set_type("Projector Room")
        done = False
        choices = ["LED", "Lamp", "RGB"]
        while not done:
            temp = input("\nEnter the projector's light source. (LED, Lamp, RGB): ")
            if temp in choices:
                self._light = temp
                done = True
            else:
                print("\nNot a valid choice. Please try again!")

        done = False
        while not done:
            temp = input("What is the width of the projector screen (in ft): ")
            try:
                self._width = float(temp)
                done = True
            except ValueError:
                print("\nNot an integer. Please try again!")

        done = False
        while not done:
            temp = input("What is the distance between the projector and screen (in ft): ")
            try:
                self._distance = float(temp)
                done = True
            except ValueError:
                print("\nNot an integer. Please try again!")

    # Throw ratio = distance / width, distance = throw ratio * width
    # Ex: distance = 1.5 * 100 = 150 inches optimal distance 
    def optimal_dist(self):
        throw_ratio = float(self._distance / self._width)
        optimal = float(throw_ratio * self._width)
        return optimal

    # Use super display as well
    def display(self):
        super().display()
        print("\nProjector Size:", self._light, "\nScreen width:", self._width, 
              "\nDistance between the projector and the screen:", self._distance,
              "\nOptimal distance projector should be placed away from screen: ",
               self.optimal_dist())

# Zoom room, has microphones, webcams, classroom meeting ID
class zoom(room):
    # Constructor
    def __init__(self):
        # Number of microhpones
        self._microphone = ""
        # Number of webcams
        self._webcam = ""
        # Classroom meeting ID
        self._meet_id = ""

    # Constructor with arguments
    def __init__(self, mic, cam, id):
        self._microphone = mic
        self._webcam = cam
        self._meet_id = id

    # Add in a new zoom classroom
    def read(self):
        super().read()
        super().set_type("Zoom Room")
        # add the number of mics available
        done = False
        while not done:
            temp = input("\nEnter the number of microphones available: ")
            try:
                self._microphone = int(temp)
                done = True
            except ValueError:
                print("Not an integer. Please try again!")

        done = False
        while not done:
            temp = input("Enter the number of webcams available: ")
            try:
                self._webcam = int(temp)
                done = True
            except ValueError:
                print("\nNot an integer. Please try again!")
        self._meet_id = input("Please enter the classroom meeting ID: ")

    # Use super display as well
    def display(self):
        super().display()
        print("\nMicrophones available:", self._microphone, "\nWebcams available:",
              self._webcam, "\nClassroom Meeting ID:", self._meet_id)

# Class course is mainly used for Program 5
# Course being offered, the day it is available, and the time
class course(room):
    # Constructor
    def __init__(self):
        self._name = None
        self._day = None
        self._time = None

    # Constructor with arguments
    def __init__(self, name, day, time):
        self._name = name
        self._day = day
        self._time = time

    # Read in information for a new class, set the day, and time
    def read(self):
        day = days()
        if day == 1:
            self._day = "Monday/Wednesday"
        if day == 2:
            self._day = "Tuesday/Thursday"
        if day == 3:
            self._day = "Wednesday/Friday"

        time = timing()
        if time == 1:
            self._time = "09:00 AM"
        if time == 2:
            self._time = "10:00 AM"
        if time == 3:
            self._time = "11:00 AM"
        if time == 4:
            self._time = "12:00 PM"
        if time == 5:
            self._time = "01:00 PM"
        if time == 6:
            self._time = "02:00 PM"
        if time == 7:
            self._time = "03:00 PM"
        if time == 8:
            self._time = "04:00 PM"
        if time == 9:
            self._time = "05:00 PM"

    # Set the course user wants
    def set_course(self, name):
        self._name = name

    # Return the course name
    def get_course(self):
        return self._name

    # Set the day
    def set_day(self, day):
        self._day = day

    # Set the time
    def set_time(self ,time):
        self._time = time

    # Display a course with info
    def display(self):
        print("\nClass:", self._name, "\nDays Meeting: " + self._day,
              "\nTime:", self._time)

    # Compare the value of a name with the name passed in with an object
    def compare(self, source):
        if self._name < source._name:
            return -1
        elif self._name > source._name:
            return 1

    # Compares with just the name, no object
    def compare_name(self, name):
        if self._name < name:
            return -1
        elif self._name > name:
            return 1