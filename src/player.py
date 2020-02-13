from item import Item

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []
        self.items =[]

    def __str__(self):
        return f"Player: {self.name}"

    def travel(self, direction):
        next_room = getattr(self.room, f"{direction}_to")
        if next_room is not None:
            self.room = next_room
            print(self.room)
        else:
            print("You cannot move in that direction")      

#  * If it is there, remove it from the `Room` contents, and add it to the
#  inventory
    def add_items(self, item):
        if (len( self.room.items)):
            self.room.items.remove(item)
            self.inventory.append(item)
            item.on_take()
        else:
            print("That item is not in this room.")

#  remove items from the inventory.
    def drop_items(self, item):
        if (len( self.inventory)):
            self.inventory.remove(item)
            self.room.items.append(item)
            item.on_drop()
        else:
            print("This item is not in your inventory.")

# view your current inventory
    def view_inventory(self):
        if len(self.inventory) > 0:
           
            print(f"Items in current inventory {self.inventory}")
        else:
            print("There are currently no items in your inventory.")