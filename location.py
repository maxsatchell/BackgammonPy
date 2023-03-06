from colours import Colours


class Location:

    def __init__(self, number=0, colour=Colours.EMPTY):
        # Set the initial number of pieces in the location to 0
        self.number = number
        # Set the initial Location setting to Empty
        self.colour = colour

    def remove_one_piece(self):
        self.number -= 1
        if self.number == 0:
            self.colour = Colours.EMPTY

    def add_one_piece(self, colour_added):
        self.number += 1
        if self.number == 1:
            self.colour = colour_added