from room import Room
from player import Player
from item import Item



# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                   ),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",),
}


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# items in the game
backpack = Item('backpack', "small backpack to hold items")
lantern = Item('lantern', "Lanter to help light your path")
sword = Item('sword', "Long blade steel sword, could come in handy")
compass = Item('compass', "compass to navigate your way")
treasure = Item('treasure', "treasure chest filled with gold coins")

# append the items to rooms
room['outside'].items.append(backpack)
room['foyer'].items.append(lantern)
room['overlook'].items.append(sword)
room['narrow'].items.append(compass)
room['treasure'].items.append(treasure)



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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


# player starts off in the outside room
player = Player(input("Please enter your name: "), room['outside'])

def move_player(move_location):
    if move_location != None:
        player.current_room = move_location
    else:
        print(f"{player.name}, looks like you may have hit a dead end, time to recalculate and head in a new direction. ")


while True:

   
# Print player name along with the current room and its description - This comes from player def_str_
    print(f'{player}')


    player_input = input(
        "~~~> Choose an option: [n] North [s] South [e] East [w] West [q] Quit\n ")
    # actions = player_input.split(" ")
    # define the directions
    # direction = {'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}
    direction = ['n', 'e', 's', 'w','g','d','v',]

    if player_input in direction:
        attempted_room = getattr(player.current_room, f"{player_input}_to")
        if attempted_room != None:
            player.change_room(attempted_room)
        else:
            print("Movement in that direction invalid")

    elif player_input == 'q':
        exit()
    else:
        print("Input not valid, please try again")

        # elif player_input[0] == 'g':
        #      player.add_items(sword)
        # elif player_input[0] == 'v':
        #      player.view_inventory()

   


   