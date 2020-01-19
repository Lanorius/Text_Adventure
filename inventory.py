class Inventory:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def show_items(self):
        for i in self.items:
            print(i.name)
