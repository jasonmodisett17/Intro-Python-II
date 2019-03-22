# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add(self, item):
        self.items.append(item)

    def itemsInventory(self):
        if len(self.items) == 0:
            return "No items in this room.\n"
        else:
            names = [item.name for item in self.items]
            return f"Items in room: {', '.join(names)}\n"

    def remove(self, item):
        self.items.remove(item)