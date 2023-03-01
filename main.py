import ast
import copy
import random

from enum import Enum
from deepdiff import DeepDiff
import pandas as pd
import numpy as np
from model import BackgammonModel



class Colours(Enum):
    WHITE = -1
    BLACK = 1
    EMPTY = 0


# Testing the crossover

def roll_dice():
    dice = random.randint(1, 6)
    return dice


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


class Board:

    def __init__(self, locations):
        self.locations = locations

    def __eq__(self, other):
        return self.locations == other.locations

    def starting_board():
        locations = {}
        locations[0] = Location(2, Colours.WHITE)
        locations[1] = Location(0, Colours.EMPTY)
        locations[2] = Location(0, Colours.EMPTY)
        locations[3] = Location(0, Colours.EMPTY)
        locations[4] = Location(0, Colours.EMPTY)
        locations[5] = Location(5, Colours.BLACK)
        locations[6] = Location(0, Colours.EMPTY)
        locations[7] = Location(3, Colours.BLACK)
        locations[8] = Location(0, Colours.EMPTY)
        locations[9] = Location(0, Colours.EMPTY)
        locations[10] = Location(0, Colours.EMPTY)
        locations[11] = Location(5, Colours.WHITE)
        locations[12] = Location(5, Colours.BLACK)
        locations[13] = Location(0, Colours.EMPTY)
        locations[14] = Location(0, Colours.EMPTY)
        locations[15] = Location(0, Colours.EMPTY)
        locations[16] = Location(3, Colours.WHITE)
        locations[17] = Location(0, Colours.EMPTY)
        locations[18] = Location(5, Colours.WHITE)
        locations[19] = Location(0, Colours.EMPTY)
        locations[20] = Location(0, Colours.EMPTY)
        locations[21] = Location(0, Colours.EMPTY)
        locations[22] = Location(0, Colours.EMPTY)
        locations[23] = Location(2, Colours.BLACK)
        locations[40] = Location(0, Colours.EMPTY)  # where exposed pieces go(black)
        locations[41] = Location(0, Colours.EMPTY)  # where exposed pieces go(white)
        locations[50] = Location(0, Colours.EMPTY)  # Where black pieces are taken off the board in end game
        locations[51] = Location(0, Colours.EMPTY)  # Where white pieces are taken off the board in end game
        return locations

    def end_board():
        locations = {}
        locations[0] = Location(2, Colours.WHITE)
        locations[1] = Location(1, Colours.BLACK)
        locations[2] = Location(14, Colours.BLACK)
        locations[3] = Location(0, Colours.EMPTY)
        locations[4] = Location(0, Colours.EMPTY)
        locations[5] = Location(0, Colours.EMPTY)
        locations[6] = Location(0, Colours.EMPTY)
        locations[7] = Location(0, Colours.EMPTY)
        locations[8] = Location(0, Colours.EMPTY)
        locations[9] = Location(0, Colours.EMPTY)
        locations[10] = Location(0, Colours.EMPTY)
        locations[11] = Location(5, Colours.WHITE)
        locations[12] = Location(0, Colours.EMPTY)
        locations[13] = Location(0, Colours.EMPTY)
        locations[14] = Location(0, Colours.EMPTY)
        locations[15] = Location(0, Colours.EMPTY)
        locations[16] = Location(3, Colours.WHITE)
        locations[17] = Location(0, Colours.EMPTY)
        locations[18] = Location(5, Colours.WHITE)
        locations[19] = Location(0, Colours.EMPTY)
        locations[20] = Location(0, Colours.EMPTY)
        locations[21] = Location(0, Colours.EMPTY)
        locations[22] = Location(0, Colours.EMPTY)
        locations[23] = Location(0, Colours.EMPTY)
        locations[40] = Location(0, Colours.EMPTY)  # where exposed pieces go(black)
        locations[41] = Location(0, Colours.EMPTY)  # where exposed pieces go(white)
        locations[50] = Location(0, Colours.EMPTY)  # Where black pieces are taken off the board in end game
        locations[51] = Location(0, Colours.EMPTY)  # Where white pieces are taken off the board in end game
        return locations

    def taken_board_test():
        locations = {}
        locations[0] = Location(2, Colours.BLACK)
        locations[1] = Location(7, Colours.BLACK)
        locations[2] = Location(2, Colours.BLACK)
        locations[3] = Location(2, Colours.BLACK)
        locations[4] = Location(2, Colours.BLACK)
        locations[5] = Location(0, Colours.EMPTY)
        locations[6] = Location(0, Colours.EMPTY)
        locations[7] = Location(0, Colours.EMPTY)
        locations[8] = Location(0, Colours.EMPTY)
        locations[9] = Location(0, Colours.EMPTY)
        locations[10] = Location(0, Colours.EMPTY)
        locations[11] = Location(5, Colours.WHITE)
        locations[12] = Location(0, Colours.EMPTY)
        locations[13] = Location(0, Colours.EMPTY)
        locations[14] = Location(0, Colours.EMPTY)
        locations[15] = Location(0, Colours.EMPTY)
        locations[16] = Location(3, Colours.WHITE)
        locations[17] = Location(0, Colours.EMPTY)
        locations[18] = Location(5, Colours.WHITE)
        locations[19] = Location(0, Colours.EMPTY)
        locations[20] = Location(0, Colours.EMPTY)
        locations[21] = Location(0, Colours.EMPTY)
        locations[22] = Location(0, Colours.EMPTY)
        locations[23] = Location(0, Colours.EMPTY)
        locations[40] = Location(0, Colours.EMPTY)  # where exposed pieces go(black)
        locations[41] = Location(2, Colours.WHITE)  # where exposed pieces go(white)
        locations[50] = Location(0, Colours.EMPTY)  # Where black pieces are taken off the board in end game
        locations[51] = Location(0, Colours.EMPTY)  # Where white pieces are taken off the board in end game
        return locations

    def end_board_test():
        locations = {}
        locations[0] = Location(0, Colours.EMPTY)
        locations[1] = Location(1, Colours.BLACK)
        locations[2] = Location(1, Colours.BLACK)
        locations[3] = Location(0, Colours.EMPTY)
        locations[4] = Location(0, Colours.EMPTY)
        locations[5] = Location(0, Colours.EMPTY)
        locations[6] = Location(0, Colours.EMPTY)
        locations[7] = Location(0, Colours.EMPTY)
        locations[8] = Location(0, Colours.EMPTY)
        locations[9] = Location(0, Colours.EMPTY)
        locations[10] = Location(0, Colours.EMPTY)
        locations[11] = Location(7, Colours.WHITE)
        locations[12] = Location(0, Colours.EMPTY)
        locations[13] = Location(0, Colours.EMPTY)
        locations[14] = Location(0, Colours.EMPTY)
        locations[15] = Location(0, Colours.EMPTY)
        locations[16] = Location(4, Colours.WHITE)
        locations[17] = Location(0, Colours.EMPTY)
        locations[18] = Location(4, Colours.WHITE)
        locations[19] = Location(0, Colours.EMPTY)
        locations[20] = Location(0, Colours.EMPTY)
        locations[21] = Location(0, Colours.EMPTY)
        locations[22] = Location(0, Colours.EMPTY)
        locations[23] = Location(0, Colours.EMPTY)
        locations[40] = Location(0, Colours.EMPTY)  # where exposed pieces go(black)
        locations[41] = Location(0, Colours.EMPTY)  # where exposed pieces go(white)
        locations[50] = Location(13, Colours.BLACK)  # Where black pieces are taken off the board in end game
        locations[51] = Location(0, Colours.EMPTY)  # Where white pieces are taken off the board in end game
        return locations

    def end_board_test_2():
        locations = {}
        locations[0] = Location(0, Colours.EMPTY)
        locations[1] = Location(1, Colours.BLACK)
        locations[2] = Location(1, Colours.BLACK)
        locations[3] = Location(0, Colours.EMPTY)
        locations[4] = Location(0, Colours.EMPTY)
        locations[5] = Location(0, Colours.EMPTY)
        locations[6] = Location(0, Colours.EMPTY)
        locations[7] = Location(0, Colours.EMPTY)
        locations[8] = Location(0, Colours.EMPTY)
        locations[9] = Location(0, Colours.EMPTY)
        locations[10] = Location(0, Colours.EMPTY)
        locations[11] = Location(7, Colours.WHITE)
        locations[12] = Location(0, Colours.EMPTY)
        locations[13] = Location(0, Colours.EMPTY)
        locations[14] = Location(0, Colours.EMPTY)
        locations[15] = Location(0, Colours.EMPTY)
        locations[16] = Location(4, Colours.WHITE)
        locations[17] = Location(0, Colours.EMPTY)
        locations[18] = Location(4, Colours.WHITE)
        locations[19] = Location(0, Colours.EMPTY)
        locations[20] = Location(0, Colours.EMPTY)
        locations[21] = Location(0, Colours.EMPTY)
        locations[22] = Location(0, Colours.EMPTY)
        locations[23] = Location(0, Colours.EMPTY)
        locations[40] = Location(0, Colours.EMPTY)  # where exposed pieces go(black)
        locations[41] = Location(0, Colours.EMPTY)  # where exposed pieces go(white)
        locations[50] = Location(13, Colours.BLACK)  # Where black pieces are taken off the board in end game
        locations[51] = Location(0, Colours.EMPTY)  # Where white pieces are taken off the board in end game
        return locations

    def end_of_game_checker(self, colour):
        adder = 0
        if colour == Colours.BLACK:
            for i in range(0, 6):
                if self.locations[i].colour == Colours.WHITE:
                    adder += 0
                else:
                    adder += self.locations[i].number
            if adder == (15 - self.locations[50].number):
                return True
            else:
                return False
        else:
            for b in range(18, 24):
                if self.locations[b].colour == Colours.BLACK:
                    adder += 0
                else:
                    adder += self.locations[b].number
            if adder == (15 - self.locations[51].number):
                return True
            else:
                return False

    def game_finished(self):
        if self.locations[50].number == 15 or self.locations[51].number == 15:
            return True
        else:
            return False

    def valid_moves(self, colour, dice_value):
        valid_moves = []
        colour_locations = []
        colour_locations_end_game_white = []
        colour_locations_end_game_black = []
        # Valid positions around on the board
        for i in range(0, 24):
            if self.locations[i].colour == colour and self.locations[i].number >= 1:
                colour_locations.append(i)
        # Valid moves the white player to move in the end game to take off
        for w in range(23, 17, -1):
            if colour == Colours.WHITE and self.locations[w].number >= 1:
                colour_locations_end_game_white.append(w)
        # Copy paste check for error
        for b in range(0, 6):
            if colour == Colours.BLACK and self.locations[b].number >= 1:
                colour_locations_end_game_black.append(b)

        # Valid moves being processed in the end game (taking off the board)
        if self.end_of_game_checker(colour):
            if colour == Colours.BLACK:
                minimum_black = self.calculate_minimum_black(dice_value, colour)
                for end_game_locations_b in colour_locations_end_game_black:
                    locator = end_game_locations_b - dice_value
                    if locator == minimum_black or locator == -1 or locator >= 0:
                        valid_moves.append(end_game_locations_b)
                return valid_moves
            else:
                maximum_white = self.calculate_maximum_white(dice_value, colour)
                for end_game_locations_w in colour_locations_end_game_white:
                    locator = end_game_locations_w + dice_value
                    if locator == maximum_white or locator == 24 or locator <= 23:
                        valid_moves.append(end_game_locations_w)
                return valid_moves
        if (colour == Colours.BLACK and self.locations[40].number >= 1) or (
                colour == Colours.WHITE and self.locations[41].number >= 1):
            if colour == Colours.BLACK and self.locations[40].number >= 1:
                locator = 23 - dice_value + 1
                # Creating the function that finds the valid locations that a player can go to when taken.
                if locator in self.locations_to_come_in_black(colour):
                    valid_moves.append(locator)
                return valid_moves
            elif colour == Colours.WHITE and self.locations[41].number >= 1:
                locator = dice_value - 1
                # Creating the function that finds the valid locations that a player can go to when taken.
                if locator in self.locations_to_come_in_white(colour):
                    valid_moves.append(locator)
                return valid_moves
        else:
            if colour == Colours.BLACK:
                for black_col_location in colour_locations:
                    locator = black_col_location - dice_value
                    if locator in self.valid_locations_pieces_can_go(colour):
                        valid_moves.append(black_col_location)
                return valid_moves
            else:
                for white_col_location in colour_locations:
                    locator = white_col_location + dice_value
                    if locator in self.valid_locations_pieces_can_go(colour):
                        valid_moves.append(white_col_location)
                return valid_moves
        # Might have to add an extra return in here

    def generate_valid_board_moves_after_one_move(self,colour,roll):
        current_board_locations = copy.deepcopy(self.locations)
        current_board_locations_2 = copy.deepcopy(self.locations)
        game_board_generator = Board(current_board_locations)
        game_board_changer = Board(current_board_locations_2)
        board_states = []
        valid_moves = game_board_generator.valid_moves(colour, roll)
        for i in range(0,len(valid_moves)):
            game_board_changer.execute_move(colour, valid_moves[i], roll)
            board_states.append(game_board_changer)
            game_board_changer = copy.deepcopy(game_board_generator)



    def generate_valid_board_states_after_both_moves_double(self, colour, roll_1, roll_2, double_board_states):
        current_board_locations = copy.deepcopy(double_board_states.locations)
        current_board_locations_2 = copy.deepcopy(double_board_states.locations)
        game_board_generator = Board(current_board_locations)
        game_board_changer = Board(current_board_locations_2)
        board_states = []
        one_roll_board_states = []
        valid_moves = game_board_generator.valid_moves(colour, roll_1)
        for i in range(0, len(valid_moves)):
            game_board_changer.execute_move(colour, valid_moves[i], roll_1)
            game_board_changer_holder = copy.deepcopy(game_board_changer)
            valid_moves_roll2 = game_board_changer.valid_moves(colour, roll_2)
            for j in range(0, len(valid_moves_roll2)):
                game_board_changer.execute_move(colour, valid_moves_roll2[j], roll_2)
                # if len(board_states) > 0:
                #     for g in range(len(board_states)):
                #         if not (DeepDiff(board_states[g], game_board_changer)):
                #             game_board_changer = copy.deepcopy(game_board_changer_holder)
                #             continue
                #
                #     if (DeepDiff(game_board_changer_holder, game_board_changer)):
                #         board_states.append(game_board_changer)
                #         game_board_changer = copy.deepcopy(game_board_changer_holder)
                # else:
                board_states.append(game_board_changer)
                game_board_changer = copy.deepcopy(game_board_changer_holder)
            one_roll_board_states.append(game_board_changer_holder)
            game_board_changer = copy.deepcopy(game_board_generator)

        game_board_changer = copy.deepcopy(game_board_generator)
        valid_moves = game_board_generator.valid_moves(colour, roll_2)
        for i in range(0, len(valid_moves)):
            game_board_changer.execute_move(colour, valid_moves[i], roll_2)
            game_board_changer_holder = copy.deepcopy(game_board_changer)
            valid_moves_roll1 = game_board_changer.valid_moves(colour, roll_1)
            for j in range(0, len(valid_moves_roll1)):
                game_board_changer.execute_move(colour, valid_moves_roll1[j], roll_1)
                # if len(board_states) > 0:
                #     for g in range(len(board_states)):
                #         check = DeepDiff(board_states[g], game_board_changer)
                #         if not (DeepDiff(board_states[g], game_board_changer)):
                #             game_board_changer = copy.deepcopy(game_board_changer_holder)
                #             continue
                #     if (DeepDiff(game_board_changer_holder, game_board_changer)):
                #         board_states.append(game_board_changer)
                #         game_board_changer = copy.deepcopy(game_board_changer_holder)
                # else:
                board_states.append(game_board_changer)
                game_board_changer = copy.deepcopy(game_board_changer_holder)
            one_roll_board_states.append(game_board_changer_holder)
            game_board_changer = copy.deepcopy(game_board_generator)
        if len(board_states) == 0:
            return one_roll_board_states
        else:
            return board_states

    # This function should return all the board states for both dice in roll.
    def generate_valid_board_states_after_both_moves(self, colour, roll_1, roll_2):
        current_board_locations = copy.deepcopy(self.locations)
        current_board_locations_2 = copy.deepcopy(self.locations)
        game_board_generator = Board(current_board_locations)
        game_board_changer = Board(current_board_locations_2)
        board_states = []
        one_roll_board_states = []
        two_roll_board_states = []
        three_roll_board_states = []
        final_double_board_states = []
        double_board_states = []
        if roll_1 == roll_2:
            # make a new function to send originally to get the double board state
            # after go through the double board state list doing the next two double rolls.
            #  collate all the moves together and return. Probably 18*18
            double_board_states = game_board_generator.generate_valid_board_states_after_both_moves_double(colour,
                                                                                                           roll_1,
                                                                                                           roll_2,
                                                                                                           game_board_changer)
            final_double_board_states = copy.deepcopy(double_board_states)
            for i in range(len(double_board_states)):
                board_state_holder = double_board_states[i].generate_valid_board_states_after_both_moves_double(colour,
                                                                                                                roll_1,
                                                                                                                roll_2,
                                                                                                                double_board_states[
                                                                                                                    i])
                for j in range(len(board_state_holder)):
                    if board_state_holder[j] not in final_double_board_states:
                        final_double_board_states.append(board_state_holder[j])

            return final_double_board_states
        else:
            # Maybe add an end clause in but that might be covered by the one roll bs
            valid_moves = game_board_generator.valid_moves(colour, roll_1)
            for i in range(0, len(valid_moves)):
                game_board_changer.execute_move(colour, valid_moves[i], roll_1)
                game_board_changer_holder = copy.deepcopy(game_board_changer)
                valid_moves_roll2 = game_board_changer.valid_moves(colour, roll_2)
                for j in range(0, len(valid_moves_roll2)):
                    game_board_changer.execute_move(colour, valid_moves_roll2[j], roll_2)
                    # if len(board_states) > 0:
                    #     for g in range(len(board_states)):
                    #         if not (DeepDiff(board_states[g], game_board_changer)):
                    #             game_board_changer = copy.deepcopy(game_board_changer_holder)
                    #             continue
                    #     if (DeepDiff(game_board_changer_holder, game_board_changer)):
                    #         board_states.append(game_board_changer)
                    #         game_board_changer = copy.deepcopy(game_board_changer_holder)
                    # else:
                    board_states.append(game_board_changer)
                    game_board_changer = copy.deepcopy(game_board_changer_holder)
                one_roll_board_states.append(game_board_changer_holder)
                game_board_changer = copy.deepcopy(game_board_generator)

            game_board_changer = copy.deepcopy(game_board_generator)
            valid_moves = game_board_generator.valid_moves(colour, roll_2)
            for i in range(0, len(valid_moves)):
                game_board_changer.execute_move(colour, valid_moves[i], roll_2)
                game_board_changer_holder = copy.deepcopy(game_board_changer)
                valid_moves_roll1 = game_board_changer.valid_moves(colour, roll_1)
                for j in range(0, len(valid_moves_roll1)):
                    game_board_changer.execute_move(colour, valid_moves_roll1[j], roll_1)
                    # if len(board_states) > 0:
                    #     for g in range(len(board_states)):
                    #         check = DeepDiff(board_states[g], game_board_changer)
                    #         if not (DeepDiff(board_states[g], game_board_changer)):
                    #             game_board_changer = copy.deepcopy(game_board_changer_holder)
                    #             continue
                    #     if (DeepDiff(game_board_changer_holder, game_board_changer)):
                    #         board_states.append(game_board_changer)
                    #         game_board_changer = copy.deepcopy(game_board_changer_holder)
                    # else:
                    board_states.append(game_board_changer)
                    game_board_changer = copy.deepcopy(game_board_changer_holder)
                one_roll_board_states.append(game_board_changer_holder)
                game_board_changer = copy.deepcopy(game_board_generator)
            if len(board_states) == 0:
                return one_roll_board_states
            else:
                return board_states

    def execute_move(self, colour, piece_location, dice_value):
        if self.game_finished():
            return
        valid_moves = self.valid_moves(colour, dice_value)
        available_locations = self.valid_locations_pieces_can_go(colour)
        available_locations_taken_white = self.locations_to_come_in_white(colour)
        available_locations_taken_black = self.locations_to_come_in_black(colour)
        minimum_black = 100
        maximum_white = 100
        if colour == Colours.BLACK:
            minimum_black = self.calculate_minimum_black(dice_value, colour)
        if colour == Colours.WHITE:
            maximum_white = self.calculate_maximum_white(dice_value, colour)
        if (colour == Colours.BLACK and piece_location - dice_value <= -1) and (
                piece_location - dice_value == minimum_black or piece_location - dice_value == -1) and self.locations[
            piece_location].colour == Colours.BLACK and self.end_of_game_checker(Colours.BLACK):
            from_location = self.locations[piece_location]
            from_location.remove_one_piece()
            to_location = self.locations[50]
            to_location.add_one_piece(Colours.BLACK)
            return
        elif (colour == Colours.WHITE and piece_location + dice_value >= 24) and (
                piece_location + dice_value == maximum_white or piece_location + dice_value == 24) and self.locations[
            piece_location].colour == Colours.WHITE and self.end_of_game_checker(Colours.WHITE):
            from_location = self.locations[piece_location]
            from_location.remove_one_piece()
            to_location = self.locations[51]
            to_location.add_one_piece(Colours.WHITE)
            return
        if colour == Colours.WHITE and self.locations[41].number >= 1 and (
                dice_value - 1) in available_locations_taken_white:
            from_location = self.locations[41]
            from_location.remove_one_piece()
            to_location = self.locations[dice_value - 1]
            if colour == Colours.WHITE and self.locations[dice_value - 1].number == 1 and self.locations[
                dice_value - 1].colour != colour:
                to_location.remove_one_piece()
                self.locations[40].add_one_piece(Colours.BLACK)
                to_location.add_one_piece(colour)
                return
            else:
                to_location = self.locations[dice_value - 1]
                to_location.add_one_piece(colour)
                return
        # Need to black returning in after being taken off next
        elif colour == Colours.BLACK and self.locations[40].number >= 1 and (
                23 - dice_value + 1) in available_locations_taken_black:
            from_location = self.locations[40]
            from_location.remove_one_piece()
            to_location = self.locations[23 - dice_value + 1]
            if colour == Colours.BLACK and self.locations[23 - dice_value + 1].number == 1 and self.locations[
                23 - dice_value + 1].colour != colour:
                to_location.remove_one_piece()
                self.locations[41].add_one_piece(Colours.WHITE)
                to_location.add_one_piece(colour)
                return
            else:
                to_location = self.locations[23 - dice_value + 1]
                to_location.add_one_piece(colour)
                return

        if len(valid_moves) == 0:
            return

        if colour == Colours.WHITE and (piece_location + dice_value) not in available_locations:
            return

        if colour == Colours.BLACK and (piece_location - dice_value) not in available_locations:
            return

        if self.locations[piece_location].colour != colour:
            return

        if colour == Colours.WHITE and (piece_location + dice_value) in available_locations:  # used when exposed

            from_location = self.locations[piece_location]
            from_location.remove_one_piece()
            to_location = self.locations[piece_location + dice_value]

            if colour == Colours.WHITE and self.locations[piece_location + dice_value].number == 1 and self.locations[
                piece_location + dice_value].colour != colour:

                to_location.remove_one_piece()
                self.locations[40].add_one_piece(Colours.BLACK)
                to_location.add_one_piece(colour)
                return

            else:
                to_location = self.locations[piece_location + dice_value]
                to_location.add_one_piece(colour)
                return
        elif colour == Colours.BLACK and (piece_location - dice_value) in available_locations:  # used when exposed

            from_location = self.locations[piece_location]
            from_location.remove_one_piece()
            to_location = self.locations[piece_location - dice_value]

            if colour == Colours.BLACK and self.locations[piece_location - dice_value].number == 1 and self.locations[
                piece_location - dice_value].colour != colour:

                to_location.remove_one_piece()
                self.locations[41].add_one_piece(Colours.WHITE)
                to_location.add_one_piece(colour)
                return

            else:
                to_location.add_one_piece(colour)
                return

        else:
            return

    def any_pieces_taken(self, colour):
        if colour == Colours.BLACK and self.locations[40].number > 0:
            return True
        elif colour == Colours.WHITE and self.locations[41].number > 0:
            return True
        else:
            return False

    def valid_locations_pieces_can_go(self, colour):
        valid_locations_pieces_can_go = []
        for i in range(0, 23):
            if self.locations[i].colour == colour or self.locations[i].number <= 1:
                valid_locations_pieces_can_go.append(i)
        return valid_locations_pieces_can_go

    def locations_to_come_in_black(self, colour):
        locations_to_come_in_black = []
        for b in range(23, 17, -1):
            if self.locations[b].colour == colour or self.locations[b].number <= 1:
                locations_to_come_in_black.append(b)
        return locations_to_come_in_black

    def locations_to_come_in_white(self, colour):
        locations_to_come_in_white = []
        for w in range(0, 6):
            if self.locations[w].colour == colour or self.locations[w].number <= 1:
                locations_to_come_in_white.append(w)
        return locations_to_come_in_white

    def calculate_minimum_black(self, die, colour):
        minimum = 5
        if self.game_finished():
            return
        if self.end_of_game_checker(colour):
            count = 0
            while True:
                if self.locations[5 - count].number <= 0:
                    minimum -= 1
                    count += 1
                else:
                    return minimum - die
                if self.locations[5 - (count - 1)].number > 0:
                    break
        return minimum - die

    def calculate_maximum_white(self, die, colour):
        maximum = 18
        if self.game_finished():
            return
        if self.end_of_game_checker(colour):
            count = 0
            while True:
                if self.locations[18 + count].number <= 0:
                    maximum += 1
                    count += 1
                else:
                    return maximum + die
                if self.locations[18 - (count - 1)].number > 0:
                    break
        return maximum + die

    # This function takes the move the player has selected and sets the board to it
    def update_board(self, move_selected, colour, dice_value):
        board_states = self.generate_valid_board_states_after_both_moves(colour, dice_value)
        return board_states[move_selected]

    def convert_to_pd(self):
        list_of_pieces = []
        list_of_colours = []
        for i in range(0,24):
            list_of_pieces.append(self.locations[i].number)
            list_of_colours.append(self.locations[i].colour.value)

        list_of_pieces.append(self.locations[40].number)
        list_of_colours.append(self.locations[40].colour.value)
        list_of_pieces.append(self.locations[41].number)
        list_of_colours.append(self.locations[41].colour.value)
        list_of_pieces.append(self.locations[50].number)
        list_of_colours.append(self.locations[50].colour.value)
        list_of_pieces.append(self.locations[51].number)
        list_of_colours.append(self.locations[51].colour.value)

        board_list = np.array(list_of_pieces + list_of_colours)
        df = pd.DataFrame([board_list])
        return df

    def convert_to_pd_with_winner(self,winner):
        list_of_pieces = []
        list_of_colours = []
        list_winner = [winner]

        for i in range(0,24):
            list_of_pieces.append(self.locations[i].number)
            list_of_colours.append(self.locations[i].colour.value)

        list_of_pieces.append(self.locations[40].number)
        list_of_colours.append(self.locations[40].colour.value)
        list_of_pieces.append(self.locations[41].number)
        list_of_colours.append(self.locations[41].colour.value)
        list_of_pieces.append(self.locations[50].number)
        list_of_colours.append(self.locations[50].colour.value)
        list_of_pieces.append(self.locations[51].number)
        list_of_colours.append(self.locations[51].colour.value)

        board_list = np.array(list_winner + list_of_pieces + list_of_colours)
        df = pd.DataFrame([board_list])
        return df


    #def convert_from_df_to_board(self,df):








class Program:
    def run_one_game(games):
        number_of_wins_black = 0
        number_of_wins_white = 0
        backgammonModel = BackgammonModel(56, 3, 10, 32)
        training_data = Program.read_history_from_file()
        backgammonModel.train(training_data)
        for i in range(0,games):
            game_board = Board(Board.end_board_test_2())
            player1 = Player(Colours.WHITE, "White", game_board)
            player2 = Player(Colours.BLACK, "Black", game_board)
            game = Game(player1, player2, player1, game_board)
            board_history = []
            Program.board_outputter(game.board)
            starting_board = copy.deepcopy(game.board)
            while not game.board.game_finished():
                game.run_neural_network(1,backgammonModel)
                board_history.append(game.board)

            if game.board.locations[50].number == 15:
                number_of_wins_black+=1
                df = starting_board.convert_to_pd_with_winner(1)
                Program.write_history_to_file(1,board_history,df)
                print("Game is finished the winner is Black")
            else:
                number_of_wins_white+=1
                df = starting_board.convert_to_pd_with_winner(-1)
                Program.write_history_to_file(-1,board_history,df)
                print("Game is finished the winner is White")
        print("The number of wins for black is " + str(number_of_wins_black))
        print("The number of wins for white is " + str(number_of_wins_white))
        print("The number of games played was " + str(games))
    def write_history_to_file(winner,board_history,df):
        for move in board_history:
            check = move.convert_to_pd_with_winner(winner)
            df = df.append(check)
        df.to_csv('game_history.csv', mode='a', index=False, header=False)

    def read_history_from_file():
        df2 = pd.read_csv("game_history.csv")
        game_history = []
        df_to_numpy = df2.to_numpy()
        i = 0
        while i < len(df_to_numpy):
            file_input = (df_to_numpy[i][0], df_to_numpy[i][1:])
            game_history.append(file_input)
            i += 1

        return game_history


    def board_outputter(current_board):
        print("---------------------------------------")
        print("| 23 22 21 20 19 18  17 16 15 14 13 12|")
        print("---------------------------------------")
        highest_piece_count = Program.get_highest_value_top_half(current_board)
        top_half_count = 0
        line = ""
        for i in range(0, highest_piece_count):
            line += "|"
            for a in range(23, 11, -1):
                if a == 17:
                    line += "|"
                if (current_board.locations[a].number - top_half_count) > 0:
                    zero_or_one = current_board.locations[a].colour
                    if zero_or_one == Colours.WHITE:
                        line += " 0 "
                    elif zero_or_one == Colours.BLACK:
                        line += " 1 "
                else:
                    line += " . "
            line += "|"
            print(line)
            line = ""
            top_half_count += 1
        print(
            "---------------------------------------   Pieces that have been taken by the other player; Black pieces = " + str(
                current_board.locations[40].number)
            + " White pieces = " + str(current_board.locations[41].number) + " B:" + str(
                current_board.locations[50].number)
            + " W:" + str(current_board.locations[51].number))
        bottom_highest_count = Program.get_highest_value_bottom_half(current_board)
        bottom_half_count = Program.get_highest_value_bottom_half(current_board)
        for i in range(0, bottom_highest_count):
            line += "|"
            for b in range(0, 12):
                if b == 6:
                    line += "|"
                if (current_board.locations[b].number - bottom_half_count) >= 0:
                    zero_or_one = current_board.locations[b].colour
                    if zero_or_one == Colours.WHITE:
                        line += " 0 "
                    elif zero_or_one == Colours.BLACK:
                        line += " 1 "
                else:
                    line += " . "
            line += "|"
            print(line)
            line = ""
            bottom_half_count -= 1
        print("---------------------------------------")
        print("| 0  1  2  3  4  5   6  7  8  9  10 11|")
        print("---------------------------------------")

    def get_highest_value_top_half(current_board):
        highestValue = 5
        for i in range(23, 11, -1):
            valueChecker = 0
            valueChecker = current_board.locations[i].number
            if valueChecker > highestValue:
                highestValue = valueChecker
        return highestValue

    def get_highest_value_bottom_half(current_board):
        highestValue = 5
        for i in range(0, 12, 1):
            valueChecker = 0
            valueChecker = current_board.locations[i].number
            if valueChecker > highestValue:
                highestValue = valueChecker
        return highestValue


class Game:

    def __init__(self, player1, player2, current_player, board):
        self.player1 = player1
        self.player2 = player2
        self.current_player = current_player
        self.board = board

    def run_neural_network(self,nnplayer,model):
        if self.board.game_finished():
            return
        roll1 = roll_dice()
        roll2 = roll_dice()
        print("Rolled " + str(roll1) + " " + str(roll2))
        # The end game checker is not working and there may be issues with min black and white for later also white issues
        if len(self.board.valid_moves(self.current_player.colour, roll1)) == 0 and \
                len(self.board.valid_moves(self.current_player.colour, roll2)) == 0:
            print("No valid moves for " + self.current_player.name +" the rolls where " + str(roll1) +" "+ str(roll2))
            Game.player_swapper(self)
            return

        copy_board = copy.deepcopy(self.board)
        copy_current_player = copy.deepcopy(self.current_player.colour)

        board_states = copy_board.generate_valid_board_states_after_both_moves(copy_current_player, roll1, roll2)
        #if self.current_player.colour.value == nnplayer:
        max_value = 0
        best_move = board_states[0]
        for i in range(0,len(board_states)):
            # get a copy of a board
            if nnplayer == 1:#choose if white or black
                value = model.predict(board_states[i].convert_to_pd(), 1)
            else:
                value = model.predict(board_states[i].convert_to_pd(), 2)#choose if white or black
            if value > max_value:
                max_value = value
                best_move = board_states[i]
        selected_move = best_move
        #else:
            #selected_move = board_states[random.randrange(0, len(board_states))]
        self.board = selected_move
        Program.board_outputter(self.board)
        Game.player_swapper(self)






    def run_human(self):# This should become run with a human the other should become
        print("Welcome to Backgammon")
        print("The player going first is " + self.current_player.name + " and there colour is " + str(
            self.current_player.colour))
        if self.board.game_finished():
            return
        roll1 = roll_dice()
        roll2 = roll_dice()

        copy_board = copy.deepcopy(self.board)
        copy_current_player = copy.deepcopy(self.current_player.colour)

        #board_states = copy_board.generate_valid_board_states_after_both_moves(copy_current_player, 6, 1)
        df = self.board.convert_to_pd()

        if len(self.board.valid_moves(self.current_player.colour, roll1)) == 0 and \
                len(self.board.valid_moves(self.current_player.colour, roll2)) == 0:
            print("No valid moves for " + self.current_player.name)
            Game.player_swapper(self)
            return

        if roll1 == roll2:
            print("You have rolled doubles")
            for i in range(1, 5):
                if self.board.game_finished():
                    return
                self.current_player.roll_selector(roll1, roll2, self.current_player, i)
                if len(self.board.valid_moves(self.current_player.colour, roll1)) == 0:
                    print("There are no moves with this roll")
                    Game.player_swapper(self)
                    return
                piece_location = self.current_player.choose_piece(roll1, self.current_player, i)
                self.board.execute_move(self.current_player.colour, piece_location, roll1)
                Program.board_outputter(self.board)
            Game.player_swapper(self)
            return
        else:
            dice_selection = self.current_player.roll_selector(roll1, roll2, self.current_player, 1)
            if dice_selection == roll1:
                if len(self.board.valid_moves(self.current_player.colour, roll1)) == 0 and len(
                        self.board.valid_moves(self.current_player.colour, roll2)) > 0:
                    self.current_player.roll_change(roll2)
                    piece_location = self.current_player.choose_piece(roll2, self.current_player, 1)
                    self.board.execute_move(self.current_player.colour, piece_location, roll2)
                    Program.board_outputter(self.board)
                    if self.board.game_finished():
                        return
                    if len(self.board.valid_moves(self.current_player.colour, roll1)) == 0:
                        print("There are no moves with this roll")
                        Game.player_swapper(self)
                        return
                    else:
                        piece_location_2 = self.current_player.choose_piece(roll1, self.current_player, 2)
                        self.board.execute_move(self.current_player.colour, piece_location_2, roll1)
                        Program.board_outputter(self.board)

                    Program.board_outputter(self.board)
                else:
                    piece_location = self.current_player.choose_piece(roll1, self.current_player, 1)
                    self.board.execute_move(self.current_player.colour, piece_location, roll1)
                    Program.board_outputter(self.board)
                    if self.board.game_finished():
                        return
                    if len(self.board.valid_moves(self.current_player.colour, roll2)) == 0:
                        print("There are no moves with this roll")
                        Game.player_swapper(self)
                        return
                    else:
                        piece_location_2 = self.current_player.choose_piece(roll2, self.current_player, 2)
                        self.board.execute_move(self.current_player.colour, piece_location_2, roll2)
                        Program.board_outputter(self.board)

                    Program.board_outputter(self.board)
            # Copy and paste may contain errors
            else:
                if len(self.board.valid_moves(self.current_player.colour, roll2)) == 0 and len(
                        self.board.valid_moves(self.current_player.colour, roll1)) > 0:
                    self.current_player.roll_change(roll1)
                    piece_location = self.current_player.choose_piece(roll1, self.current_player, 1)
                    self.board.execute_move(self.current_player.colour, piece_location, roll1)
                    Program.board_outputter(self.board)
                    if self.board.game_finished():
                        return
                    if len(self.board.valid_moves(self.current_player.colour, roll2)) == 0:
                        print("There are no moves with this roll")
                        Game.player_swapper(self)
                        return
                    else:
                        piece_location_2 = self.current_player.choose_piece(roll2, self.current_player, 2)
                        self.board.execute_move(self.current_player.colour, piece_location_2, roll2)
                        Program.board_outputter(self.board)

                    Program.board_outputter(self.board)
                else:
                    piece_location = self.current_player.choose_piece(roll2, self.current_player, 1)
                    self.board.execute_move(self.current_player.colour, piece_location, roll2)
                    Program.board_outputter(self.board)
                    if self.board.game_finished():
                        return
                    if len(self.board.valid_moves(self.current_player.colour, roll1)) == 0:
                        print("There are no moves with this roll")
                        Game.player_swapper(self)
                        return
                    else:
                        piece_location_2 = self.current_player.choose_piece(roll1, self.current_player, 2)
                        self.board.execute_move(self.current_player.colour, piece_location_2, roll1)
                        Program.board_outputter(self.board)

                    Program.board_outputter(self.board)
        Game.player_swapper(self)

    def player_swapper(self):

        if self.current_player == self.player1:
            self.current_player = self.player2

        else:
            self.current_player = self.player1


if __name__ == '__main__':
    Program.run_one_game(3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
