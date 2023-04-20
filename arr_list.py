'''
    Israel Ayala
    03/09/2023
    Structures the node class and the linked list class.
    Uses numpy to create an array of linked lists in main...
    - Recursive function begins with a call to self
'''
from classroom import *

# Node class for a linked list
class node:
    # Constructor
    def __init__(self):
        self._room = None
        self._next = None

    # Constructor with argument
    def __init__(self, room):
        self._room = room
        self._next = None

    def set_next(self, next):
        self._next = next

    def get_next(self):
        return self._next
    
    def set_data(self, room):
        self._room = room

    def get_data(self):
        return self._room
    
# Linked list
class linked_list(node):
    # Constructor
    def __init__(self):
        self._head = None

    # Add a new node to the list
    def insert(self, room):
        if not self._head:
            self._head = node(room)
            return 1
        else:
            self._insert(room, self._head)
           
    # Recursive add, data and head
    def _insert(self, room, head):
        if not head.get_next():
            head.set_next(node(room))
            return 1
        else:
            self._insert(room, head.get_next())

    # Display the list
    def display(self):
        if not self._head:
            print("\nList is empty.\nNothing to display.")
        else:
            self._display(self._head)
    
    # Recursive display
    def _display(self, head):
        if not head:
            return 
        # Check if the data is of datatype room
        # Not really required with a hierarchy
        if isinstance(head.get_data(), room):
            head.get_data().display()
        if isinstance(head.get_data(), course):
            head.get_data().display()

        # Recursion
        self._display(head.get_next())

    # Delete the last node
    def delete(self):
        # If there is no data return false
        if not self._head:
            print("\nList is empty.\nNothing to Remove.")
            return None

        # If there is one node set to None
        if self._head.get_next() == None:
            self._head = None
            return None

        # Recursive call
        self._delete(self._head)

    # Recursive delete
    def _delete(self, head):
        if not head.get_next().get_next():
            head.set_next(None)
            return head

        self._delete(head.get_next())