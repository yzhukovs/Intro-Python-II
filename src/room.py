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
        return f"{self.name}\n\n {self.description}\n\n You have: {self.items}"
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
     

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)        

#class Room(Empty_Room):
#   def __init__(self, name, description, *items):
#        super().__init__(name, description)
#        self.items = [x for i in items]
