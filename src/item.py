# items for the game



class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def __repr__(self):
        return f"{self.item_name}, {self.item_description}"

# Add an `on_take` method to `Item`.
#   Call this method when the `Item` is picked up by the player.
#   `on_take` should print out "You have picked up [NAME]" when you pick up an item.
#   The `Item` can use this to run additional code when it is picked up.
    def on_take(self):
        print(f'You have picked up a {self.item_name}.')

# Add an `on_drop` method to `Item`. Implement it similar to `on_take`.
    def on_drop(self):
        print(f'You have dropped {self.item_name}.')