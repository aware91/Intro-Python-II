# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def move(self, direction):
        linked_room = self.current_room.other_rooms(direction)
        if linked_room is not None and len(linked_room.items) < 0:
            self.current_room = linked_room
            print(f"\nYou have entered the {linked_room.name}. {linked_room.description}\n\n")
        elif linked_room is not None and len(linked_room.items) > 0:
            self.current_room = linked_room
            print(f"\nYou have entered the {linked_room.name}. {linked_room.description}\nUpon further inspection your notice a item scattered about:\n{linked_room.items}\n\n")
        else:
            print(f"\nThat direction is not available. Try Again!!\n")