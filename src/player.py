# from item import Itemq

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
# def take_items(self, item_name):
#     item_in_room = self.current_room.get_items()
#     if(len(item_in_room)):
#         for item in items_in_room:
#             if(item.item_name == item_name):
#                 self.current_room.items.remove(item)
#                 self.inventory.append(item)
#                 item.on_take()
#         return print(f'There is no item "{item_name}" in the {self.current_room.name}')

    def add_items(self, item_name):
        items_in_room = self.room.get_items()
        if (len(items_in_room)):
            for item in items_in_room:
                if(item.item_name):
                    self.room.items.remove(item)
                    self.inventory.append(item)
                    item.on_take()
        else:
            print("That item is not in this room.")

#  remove items from the inventory.
    def drop_items(self, names):
        if(len(self.inventory)):
            for items in self.inventory:
                if(items.item_name):
                    self.room.items.append(items)
                    self.inventory.remove(items)
                    items.on_drop()
                else:
                    print('that item is not in your inventory')



    # def drop_items(self, items):
    #     if (len( self.inventory)):
    #         self.inventory.remove(items)
    #         self.room.items.append(items)
    #         items.on_drop()
    #     else:
    #         print("This item is not in your inventory.")

# view your current inventory
    def view_inventory(self):
        if len(self.inventory) > 0:
           
            print(f"Items in current inventory {self.inventory}")
        else:
            print("There are currently no items in your inventory.")
