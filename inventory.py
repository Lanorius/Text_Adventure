class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def show_items(self):
        for i in self.items:
            print(i.name)
        if len(self.items) == 0:
            print("You have no items at the moment.")
