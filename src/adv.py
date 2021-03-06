from room import Room
from player import Player
from item import Item

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

# Declare all items

item = {
    'rock': Item("rock", "A large stone might be great as a weapon or weight"),

    'lantern': Item("lantern", "A dim lantern looks like won't last for very long without more fuel"),

    'key': Item("key", "A key... Wonder what it opens?"),

    'coin': Item("coin", "A gold coin. Looks like whoever took the treasure missed something on the way out."),
}

# Add items to rooms

room['outside'].add(item['rock'])
room['narrow'].add(item['lantern'])
room['foyer'].add(item['key'])
room['treasure'].add(item['coin'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

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

while True:

    # Presents info about current location, room inventory, player inventory and what can be done next.
    print("\n")
    print(player.roomCurrentlyIn.name)
    print("----------------------------")
    print(player.roomCurrentlyIn.description)
    print(player.roomCurrentlyIn.itemsInventory())
    print(player.inventory())
    print("Things you can do: move (n, s, w, e), quit (q) or action (take/drop item)\n")
    userInput = input(">> What would you like to do? ")

    inputWords = userInput.split(' ')

    if len(inputWords) == 1:
        if userInput in ['n', 'north']:
            player.move_n()
        elif userInput in ['s', 'south']:
            player.move_s()
        elif userInput in ['w', 'west']:
            player.move_w()
        elif userInput in ['e', 'east']:
            player.move_e()
        elif userInput in ['q', 'quit']:
            quit()
        elif userInput in ['i', 'inventory']:
            print(player.inventory())
        else:
            print("\nLooks like that's not a direction.")
    elif len(inputWords) == 2:
        if inputWords[0] == "get" or inputWords[0] == "take":
            for item in player.roomCurrentlyIn.items:
                if item.name == inputWords[1]:
                    player.roomCurrentlyIn.remove(item)
                    player.get(item)
                    item.on_take()
                else:
                    print("\nNo item by that name exists.")
        elif inputWords[0] == "drop":
            for item in player.items:
                if item.name == inputWords[1]:
                    player.drop(item)
                    item.on_drop()
                    player.roomCurrentlyIn.add(item)
    else:
        print("\nNot a valid input. Try again.")