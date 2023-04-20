'''
    Israel Ayala
    03/15/2023
    bst file structures a binary search tree with classroom data.
    duplicate data will go into a linear linked list.
'''
from classroom import *
from arr_list import *

# Node class for a BST
class b_node:
    # Constructor
    def __init__(self):
        self._name = None
        self._left = None
        self._right = None
        # Linked list head
        self._head = None

    # Constructor with argument
    def __init__(self, name):
        self._name = name
        self._left = None
        self._right = None
        self._head = None

    # Set left
    def set_left(self, left):
        self._left = left

    # Get left
    def get_left(self):
        return self._left

    # Set right
    def set_right(self, right):
        self._right = right

    # Get right
    def get_right(self):
        return self._right

    # Set data
    def set_data(self, name):
        self._name = name

    # Get data
    def get_data(self):
        return self._name

# bst class, insert duplicate data into a linked list
# has insert, search, removal, display
class bst:
    # Constructor
    def __init__(self):
        self._root = None

    # Insert into the tree, need a compare function in the base class
    # will determine if we go to the left or the right 
    def insert(self, name):
        if not self._root:
            # Will set the data and left and right to None
            self._root = b_node(name)
            return 1
        # Otherwise, call recursive function
        self._insert(self._root, name)

    # Recursive insert
    def _insert(self, root, name):
        #if root is None:
        if root is None:
            root = b_node(name)
            return root
            
        # If the type of classroom is the same, add to a linked list
        if root.get_data().get_course() == name.get_course():
            if root._head is None:
                root._head = linked_list()
            root._head.insert(name)
            return 1

        # Otherwise, if the data passed in is smaller than root
        if root.get_data().compare(name) == -1:
            # Go to the left
            self._insert(root.get_left(), name)
        else:
            # Otherwise, go to the right
            self._insert(root.get_right(), name)

    # Display the whole tree
    def display(self):
        if self._root is None:
            print("\nList is empty!\nNothing to display")
            return None
        
        self._display(self._root)

    # Recursive display
    def _display(self, root):
        if root is None:
            return None
        
        self._display(root.get_left())
        root.get_data().display()
        # Display the linked list
        if root._head:
            root._head.display()
        self._display(root.get_right())

    # Display all classrooms of a given course name
    def display_type(self, name):
        if self._root is None:
            print("\nList is empty!\nNothing to display.")
            return None
        
        self._display_type(self._root, name)

    # Recursive 
    def _display_type(self, root, name):
        if root is None:
            return None
        
        # Start with the left
        self._display_type(root.get_left(), name)
        # If the classroom is the same
        if root.get_data().get_course() == name:
            # Display
            root.get_data().display()
            # Display the linked list
            if root._head:
                root._head.display()

        # Go to the right
        self._display_type(root.get_right(), name)

    # Remove a node by name
    def remove(self, name):
        if self._root is None:
            print("\nList is empty! \nNothing to remove.")
            return None
        
        self._remove(self._root, name)

    def _remove(self, root, name):
        if root is None:
            print("\nList is empty! \nNothing to remove.")
            return None

        if root.get_data().compare_name(name) == -1:
            root.set_left(self._remove(root.get_left(), name))
        elif root.get_data().compare_name(name) == 1:
            root.set_right(self._remove(root.get_right(), name))

        # Check for linked list
        if root._head is not None:
            # Remove from linked list
            root._head.remove(name)

        if root.get_left() is None:
            temp = root.get_right()
            root = None
            return temp
        elif root.get_right() is None:
            temp = root.get_left()
            root = None
            return temp