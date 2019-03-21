# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []
    def moving(self, direction):
        if direction in ["n", "N","s","S","e", "E", "w", "W"]:
            next_room = self.current_room.get_direction(direction)
            if next_room is not None:
                self.current_room = next_room
            else: 
                print("You cannot move in that direction")


    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)    
