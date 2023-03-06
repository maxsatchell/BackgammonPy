class Player:

    def __init__(self, colour, name, board):
        self.colour = colour
        self.name = name
        self.board = board

    def output_dice(self, roll1, roll2):
        print("you rolled a " + str(roll1) + " and a " + str(roll2))

    def roll_selector(self, roll1, roll2, current_player, move_count):
        self.output_dice(roll1, roll2)
        if roll1 == roll2:
            print("You rolled doubles that means that you get 4 throws")
            return roll1
        while (True):
            print("Select the dice that you would like to use first.")
            # I have changed for greater than in the logic of these next two ifs refer back if this is incorrect
            if len(self.board.valid_moves(current_player.colour, roll1)) == 0 and len(
                    self.board.valid_moves(current_player.colour, roll2)) > 0:
                print("You have not got any available moves with " + str(roll1))
                print("Please select the dice " + str(roll2) + " to begin with")
            elif len(self.board.valid_moves(current_player.colour, roll2)) == 0 and len(
                    self.board.valid_moves(current_player.colour, roll1)) > 0:
                print("You have not got any available moves with " + str(roll2))
                print("Please select the dice " + str(roll1) + " to begin with")
            dice_picker = input("To select the dice you would like to use first press the number that it is : ")
            dice_check_one = str(roll1)
            dice_check_two = str(roll2)
            if dice_picker == dice_check_one:
                print("You have selected the dice " + dice_check_one + " your next roll will be with " + dice_check_two)
                return roll1
            elif dice_picker == dice_check_two:
                print("You have selected the dice " + dice_check_two + " your next roll will be with " + dice_check_one)
                return roll2
            else:
                print("Invalid selection please try again")

    def choose_piece(self, roll, current_player, movecount):
        valid_moves = self.board.valid_moves(current_player.colour, roll)
        location_identifier = 0
        while True:
            if self.board.any_pieces_taken(current_player.colour):
                print(
                    "YOUR PIECE HAS BEEN TAKEN choose a valid location to come back onto the board with the dice rolled")
            print("The dice chosen for this move is " + str(roll))
            piece_location = input(
                "Select a piece from the Board to move. E.G. press 1 to move the pieces in location 1 :")
            location_identifier = int(piece_location)
            if location_identifier in valid_moves:
                return location_identifier
            else:
                print("Invalid selection please restart")

    def roll_change(self, roll):
        print("There are no available moves on the dice you have selected!")
        print("But there are available moves with the other roll " + str(roll))
        print(str(roll) + " is the dice you have now selected")