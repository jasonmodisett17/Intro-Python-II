# Write a class to hold player information, e.g. what room they are in
# currently.

from room import Room


class Player:
    def __init__(self, room):
        self.roomCurrentlyIn = room
        self.items = []

    def move_n(self):
        if hasattr(self.roomCurrentlyIn, 'n_to'):
            newRoom = self.roomCurrentlyIn.n_to
            self.roomCurrentlyIn = newRoom
        else:
            print("\nCan't go in that direction!")

    def move_s(self):
        if hasattr(self.roomCurrentlyIn, 's_to'):
            newRoom = self.roomCurrentlyIn.s_to
            self.roomCurrentlyIn = newRoom
        else:
            print("\nCan't go in that direction!")

    def move_w(self):
        if hasattr(self.roomCurrentlyIn, 'w_to'):
            newRoom = self.roomCurrentlyIn.w_to
            self.roomCurrentlyIn = newRoom
        else:
            print("\nCan't go in that direction!")

    def move_e(self):
        if hasattr(self.roomCurrentlyIn, 'e_to'):
            newRoom = self.roomCurrentlyIn.e_to
            self.roomCurrentlyIn = newRoom
        else:
            print("\nCan't go in that direction!")

    def get(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)

    def inventory(self):
        if len(self.items) == 0:
            return "No items in inventory."
        else:
            names = [item.name for item in self.items]
            return f"Items in your inventory: {', '.join(names)}"
