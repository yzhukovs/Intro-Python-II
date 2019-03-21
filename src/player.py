# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []
    def moving(self, direction):
        if direction in ["n", "s", "e", "w"]:
            next_room = self.current_room.get_direction(direction)
            if next_room is not None:
                self.current_room = next_room
                print(self.current_room)
            else:
                print("You cannot move in that direction.")


    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        for i in self.items:
            if i.name == item:
                self.items.remove(i)  

    def inventory(self):
        if len(self.items) == 0:
            return "No items in inventory."
        else: 
            names = [item.name for item in self.items]
            return f"Items in your inventory: {', '.join(names)}"