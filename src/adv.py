from player import Player
from room import Room
from item import Item
import textwrap
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

items = { 
    'key': Item("magic key", "opens the magic door to exit")
}

player = Player("name", room['outside'])
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
#player = Player(room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print(textwrap.dedent(f"You are currently in room:{player.current_room.name}"))
print(textwrap.fill(player.current_room.description))
print(" ")
print(textwrap.dedent('''
        Where would you like to go?
        Type [go north] To go North [go east] To go East [go south] To go South [w] To go West
        Also you can 'take <ItemName>' or 'put <ItemName>' in your inventory
        and 'drop <ItemName>' to remove item from your inventory example: "take coins" or "drop sword".
        Press 'i' to show inventory of items or press 'q' to quit
    '''))

while True:
    cmd = input(">").lower()
    if len(cmd) > 1:
        cmd = input("\nInvalid Entry")
    if len(cmd) == 1:
        if cmd == "q":
            print("You left the game, goodbye!")
            break
    if cmd == "i":
        print(player.items)          
    elif cmd == "w":
        player.moving(cmd)
        print(textwrap.dedent(f"You are currently in room: {player.current_room.name}"))
    elif cmd == "n":
        player.moving(cmd)
        print(textwrap.dedent(f"You are currently in room: {player.current_room.name}"))   
    elif cmd == "e":
        player.moving(cmd)
        print(textwrap.dedent(f"You are currently in room: {player.current_room.name}")) 
    elif cmd == "s":
        player.moving(cmd)
        print(textwrap.dedent(f"You are currently in room: {player.current_room.name}")) 
    else:
        long_cmd = cmd.split()
        if len(long_cmd) == 2:
            if long_cmd[0] == 'put' or long_cmd[0] == 'take':
                for item in player.current_room.items:
                    if long_cmd[1] == item.name:
                        player.current_room.remove_item(item)
                        player.remove_item(item)
                        item.taking()
            else:
                print("The item is not available in the room")
            if long_cmd[0] == 'drop':
                for item in player.items:
                    if long_cmd[1] == item.name:
                        player.remove_item(item)
                        player.current_room.add_item(item)
                        item.dropping()
                    
        else:
            print("Error please enter a valid command")






