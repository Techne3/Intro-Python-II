# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return (f'Player: {self.name} \n Location: {self.current_room.name} \n {self.current_room.description}')

#   def change_room(self, new_room):
#         self.current_room = new_room
