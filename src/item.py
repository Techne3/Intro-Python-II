# items for the game



class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def __repr__(self):
        return f"{self.item_name}, {self.item_description}"


    def on_take(self):
        print(f'You have picked up a {self.item_name}.')


    def on_drop(self):
        print(f'You have dropped {self.item_name}.')