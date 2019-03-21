# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
        if items is None:
            self.items = []
        else: 
            self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    def __repr__(self):
        room_string = f"{self.name}\n\n"
        room_string += f"{self.description}\n\n"    
        room_string += f"Exits: {self.get_exits()}"
        if len(self.items) > 0:
            room_string += f"You see {self.get_item_string()}"      
        return room_string
    def get_item_string(self):
        return ','.join([str(i) for i in self.items])    
    def get_exits(self):
        exits = []
        if self.n_to is not None:
            exits.append('n')
        if self.e_to is not None:
            exits.append('e')
        if self.s_to is not None:
            exits.append('s') 
        if self.w_to is not None:
            exits.append('w')  
        return ", ".join(exits)     
    def get_direction(self, direction):
        if direction == "n":
            return self.n_to
        if direction == "s":
            return self.s_to   
        if direction == "e":
            return self.e_to
        if direction == "w":
            return self.w_to
        else:
            return None   
    def find_item_by_string(self, item_name):
        item_names = [item.name for item in self.items]
        print(item_names)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_to_remove):
        for item_in_room in self.items:
            if item_in_room.name.lower() == item_to_remove.name.lower():
                self.items.remove(item_to_remove)
                break        

#class Room(Empty_Room):
#   def __init__(self, name, description, *items):
#        super().__init__(name, description)
#        self.items = [x for i in items]
