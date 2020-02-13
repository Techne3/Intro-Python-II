# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

        # directions
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None

     def get_items(self):
        if len(self.items) > 0:
            print(f"Items in the room: ")
            for item in self.items:
                print(item)
        else:
            print("There are no items in the room");


    def add_item(self, item):
        self.items.append(item)       

    def see_room(self):
        print(f"Items in this room: {self.items}")