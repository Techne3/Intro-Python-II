from room import Room
from player import Player

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

def move_player(next_room):
    if next_room != None:
        player.current_room = next_room
    else:
        print(f"{player.name}, looks like you may have hit a dead end, time to recalculate and head in a new direction. ")


while True:

   
# Print player name along with the current room and its description - This comes from player def_str_
    print(f'{player}')

    player_input = input(
        "~~~> Choose your destination: [n] North [s] South [e] East [w] West [q] Quit\n ")
    # define the directions
    # direction = {'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}
    direction = {'n', 'e', 's', 'w'}

    # game logic 
    if player_input in direction:
        if player_input[0] == 'n':
            move_player(player.current_room.n_to)
        elif player_input[0] == 's':
            move_player(player.current_room.s_to)
        elif player_input[0] == 'e':
            move_player(player.current_room.e_to)
        elif player_input[0] == 'w':
            move_player(player.current_room.w_to)
        # player.current_room = getattr(
        #     player.current_room, direction[player_input])
    elif(player_input == 'q'):
        print("\n Rest up for the next quest")
        exit()
    else:
        print('INVALID OPTION, please select another option')
