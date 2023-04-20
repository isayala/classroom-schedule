'''
    Israel Ayala
    03/09/2023
    Test the classroom file.
    The first test is test_read() which is for the read in function
    from the base class. Two ingegers are expected for the data members
    room, for the room number, and seats, for the number of seats.
'''
from classroom import *
from pytest import *


# Test operator +, cannot have more than 100 seats
def test_add_seats():
    room_1 = room("","",30)
    room_2 = room("","",60)

    total_seats = room_1 + room_2

    assert total_seats <= 100

# Test the read in function from base class(room)
# The purpose of this test is to ensure that expected
# data members are integers (room, seats).
def test_read():
    new_room = room("","","")

    user_input = [123, "Labroom", 40]

    monkeypatch = MonkeyPatch()
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop(0))

    new_room.read()

    # Test room integer
    assert isinstance(new_room.get_room(), int)
    # Test seats integer
    assert isinstance(new_room.get_seats(), int)

# Test set type for classroom
def test_set_type():
    new_room = room("","","")
    new_room.set_type("Computer Lab Room")
    assert new_room.get_type() == "Computer Lab Room"

# Test get room number for classroom
def test_get_room():
    new_room = room(150,"","")

    assert new_room.get_room() == 150

# Test get seats 
def test_set_seats():
    new_room = room("","",22)

    assert new_room.get_seats() == 22 

# Test the optimal distance that a projector should be 
# placed away from the screen. This can be calculated
# with the throw ratio: distance / width. Then distance * throw
def test_optimal_distance():
    distance = 10
    width = 15

    throw_ratio = float(distance/width)
    optimal = float(throw_ratio * width)

    proj_room = projector("",width,distance)

    assert proj_room.optimal_dist() == optimal