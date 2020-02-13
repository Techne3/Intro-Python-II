# Write a class to hold player information, e.g. what room they are in
# currently.
# from room import Room

from item import Item

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def change_room(self, move_room):
        self.current_room = move_room

    def __str__(self):
        return (f'Player: {self.name} \n Location: {self.current_room.name} \n {self.current_room.description} ')

    def add_items(self, item):
        if item in self.current_room.items:
            self.current_room.items.remove(item)
            self.inventory.append(item)
            item.on_take()
        else:
            print("That item is not in this room.")


    def view_inventory(self):
        if len(self.inventory) > 0:
            for i in self.inventory:
                print(self.inventory)
        else:
            print("There are no items in your inventory.")

