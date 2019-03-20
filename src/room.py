# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []


#class Room(Empty_Room):
#   def __init__(self, name, description, *items):
#        super().__init__(name, description)
#        self.items = [x for i in items]
