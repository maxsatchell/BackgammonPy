import copy

from location import Location
from colours import Colours
import pandas as pd
import numpy as np

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
        locations[0] = Location(2, Colours.BLACK)
        locations[1] = Location(2, Colours.BLACK)
        locations[2] = Location(2, Colours.BLACK)
        locations[3] = Location(3, Colours.BLACK)
        locations[4] = Location(4, Colours.BLACK)
        locations[5] = Location(2, Colours.BLACK)
        locations[6] = Location(0, Colours.EMPTY)
        locations[7] = Location(0, Colours.EMPTY)
        locations[8] = Location(0, Colours.EMPTY)
        locations[9] = Location(0, Colours.EMPTY)
        locations[10] = Location(0, Colours.EMPTY)
        locations[11] = Location(0, Colours.EMPTY)
        locations[12] = Location(0, Colours.EMPTY)
        locations[13] = Location(0, Colours.EMPTY)
        locations[14] = Location(0, Colours.EMPTY)
        locations[15] = Location(0, Colours.EMPTY)
        locations[16] = Location(0, Colours.EMPTY)
        locations[17] = Location(1, Colours.WHITE)
        locations[18] = Location(0, Colours.EMPTY)
        locations[19] = Location(3, Colours.WHITE)
        locations[20] = Location(2, Colours.WHITE)
        locations[21] = Location(1, Colours.WHITE)
        locations[22] = Location(8, Colours.WHITE)
        locations[23] = Location(0, Colours.EMPTY)
        locations[40] = Location(0, Colours.EMPTY)  # where exposed pieces go(black)
        locations[41] = Location(0, Colours.EMPTY)  # where exposed pieces go(white)
        locations[50] = Location(0, Colours.EMPTY)  # Where black pieces are taken off the board in end game
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

    def end_board_test_3():
        locations = {}
        locations[0] = Location(1, Colours.WHITE)
        locations[1] = Location(2, Colours.BLACK)
        locations[2] = Location(1, Colours.BLACK)
        locations[3] = Location(0, Colours.EMPTY)
        locations[4] = Location(2, Colours.BLACK)
        locations[5] = Location(2, Colours.BLACK)
        locations[6] = Location(1, Colours.WHITE)
        locations[7] = Location(1, Colours.BLACK)
        locations[8] = Location(0, Colours.EMPTY)
        locations[9] = Location(0, Colours.EMPTY)
        locations[10] = Location(0, Colours.EMPTY)
        locations[11] = Location(5, Colours.WHITE)
        locations[12] = Location(4, Colours.BLACK)
        locations[13] = Location(0, Colours.EMPTY)
        locations[14] = Location(0, Colours.EMPTY)
        locations[15] = Location(0, Colours.EMPTY)
        locations[16] = Location(0, Colours.EMPTY)
        locations[17] = Location(2, Colours.BLACK)
        locations[18] = Location(5, Colours.WHITE)
        locations[19] = Location(0, Colours.EMPTY)
        locations[20] = Location(0, Colours.EMPTY)
        locations[21] = Location(0, Colours.EMPTY)
        locations[22] = Location(1, Colours.WHITE)
        locations[23] = Location(2, Colours.WHITE)
        locations[40] = Location(0, Colours.EMPTY)  # where exposed pieces go(black)
        locations[41] = Location(0, Colours.EMPTY)  # where exposed pieces go(white)
        locations[50] = Location(0, Colours.EMPTY)  # Where black pieces are taken off the board in end game
        locations[51] = Location(0, Colours.EMPTY)  # Where white pieces are taken off the board in end game
        return locations

    def end_board_test_empty():
        locations = {}
        locations[0] = Location(0, Colours.EMPTY)
        locations[1] = Location(0, Colours.EMPTY)
        locations[2] = Location(0, Colours.EMPTY)
        locations[3] = Location(0, Colours.EMPTY)
        locations[4] = Location(0, Colours.EMPTY)
        locations[5] = Location(0, Colours.EMPTY)
        locations[6] = Location(0, Colours.EMPTY)
        locations[7] = Location(0, Colours.EMPTY)
        locations[8] = Location(0, Colours.EMPTY)
        locations[9] = Location(0, Colours.EMPTY)
        locations[10] = Location(0, Colours.EMPTY)
        locations[11] = Location(0, Colours.EMPTY)
        locations[12] = Location(0, Colours.EMPTY)
        locations[13] = Location(0, Colours.EMPTY)
        locations[14] = Location(0, Colours.EMPTY)
        locations[15] = Location(0, Colours.EMPTY)
        locations[16] = Location(0, Colours.EMPTY)
        locations[17] = Location(0, Colours.EMPTY)
        locations[18] = Location(0, Colours.EMPTY)
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

    def end_board_test_4():
        locations = {}
        locations[0] = Location(7, Colours.BLACK)
        locations[1] = Location(0, Colours.EMPTY)
        locations[2] = Location(0, Colours.EMPTY)
        locations[3] = Location(2, Colours.BLACK)
        locations[4] = Location(0, Colours.EMPTY)
        locations[5] = Location(2, Colours.BLACK)
        locations[6] = Location(0, Colours.EMPTY)
        locations[7] = Location(0, Colours.EMPTY)
        locations[8] = Location(0, Colours.EMPTY)
        locations[9] = Location(0, Colours.EMPTY)
        locations[10] = Location(0, Colours.EMPTY)
        locations[11] = Location(0, Colours.EMPTY)
        locations[12] = Location(0, Colours.EMPTY)
        locations[13] = Location(0, Colours.EMPTY)
        locations[14] = Location(0, Colours.EMPTY)
        locations[15] = Location(0, Colours.EMPTY)
        locations[16] = Location(0, Colours.EMPTY)
        locations[17] = Location(0, Colours.EMPTY)
        locations[18] = Location(0, Colours.EMPTY)
        locations[19] = Location(0, Colours.EMPTY)
        locations[20] = Location(0, Colours.EMPTY)
        locations[21] = Location(0, Colours.EMPTY)
        locations[22] = Location(0, Colours.EMPTY)
        locations[23] = Location(1, Colours.WHITE)
        locations[40] = Location(0, Colours.EMPTY)  # where exposed pieces go(black)
        locations[41] = Location(0, Colours.EMPTY)  # where exposed pieces go(white)
        locations[50] = Location(4, Colours.BLACK)  # Where black pieces are taken off the board in end game
        locations[51] = Location(14, Colours.WHITE)  # Where white pieces are taken off the board in end game
        return locations

    def end_board_test_5():
        locations = {}
        locations[0] = Location(3, Colours.BLACK)
        locations[1] = Location(0, Colours.EMPTY)
        locations[2] = Location(3, Colours.BLACK)
        locations[3] = Location(1, Colours.BLACK)
        locations[4] = Location(0, Colours.EMPTY)
        locations[5] = Location(0, Colours.EMPTY)
        locations[6] = Location(0, Colours.EMPTY)
        locations[7] = Location(0, Colours.EMPTY)
        locations[8] = Location(0, Colours.EMPTY)
        locations[9] = Location(0, Colours.EMPTY)
        locations[10] = Location(0, Colours.EMPTY)
        locations[11] = Location(0, Colours.EMPTY)
        locations[12] = Location(0, Colours.EMPTY)
        locations[13] = Location(4, Colours.BLACK)
        locations[14] = Location(1, Colours.BLACK)
        locations[15] = Location(0, Colours.EMPTY)
        locations[16] = Location(1, Colours.BLACK)
        locations[17] = Location(0, Colours.EMPTY)
        locations[18] = Location(7, Colours.WHITE)
        locations[19] = Location(2, Colours.BLACK)
        locations[20] = Location(0, Colours.EMPTY)
        locations[21] = Location(0, Colours.EMPTY)
        locations[22] = Location(4, Colours.WHITE)
        locations[23] = Location(1, Colours.WHITE)
        locations[40] = Location(0, Colours.EMPTY)  # where exposed pieces go(black)
        locations[41] = Location(0, Colours.EMPTY)  # where exposed pieces go(white)
        locations[50] = Location(0, Colours.EMPTY)  # Where black pieces are taken off the board in end game
        locations[51] = Location(3, Colours.WHITE)  # Where white pieces are taken off the board in end game
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
            if self.locations[w].colour == Colours.WHITE and self.locations[w].number >= 1:
                colour_locations_end_game_white.append(w)
        # Copy paste check for error
        for b in range(0, 6):
            if self.locations[b].colour == Colours.BLACK and self.locations[b].number >= 1:
                colour_locations_end_game_black.append(b)

        # Valid moves being processed in the end game (taking off the board)
        if self.end_of_game_checker(colour):
            if colour == Colours.BLACK:
                minimum_black = self.calculate_minimum_black(dice_value, colour)
                for end_game_locations_b in colour_locations_end_game_black:
                    locator = end_game_locations_b - dice_value
                    if locator == minimum_black or locator == -1 or locator >=0:
                        if 0 <= locator <= 23:
                            if self.locations[locator].colour == Colours.WHITE:
                                continue
                        valid_moves.append(end_game_locations_b)
                return valid_moves
            else:
                maximum_white = self.calculate_maximum_white(dice_value, colour)
                for end_game_locations_w in colour_locations_end_game_white:
                    locator = end_game_locations_w + dice_value
                    if locator == maximum_white or locator == 24 or locator <=23:
                        if  0 <= locator <=23:
                            if self.locations[locator].colour == Colours.BLACK:
                                continue
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
            #final_double_board_states = copy.deepcopy(double_board_states)
            for i in range(len(double_board_states)):
                board_state_holder = double_board_states[i].generate_valid_board_states_after_both_moves_double(colour,
                                                                                                                roll_1,
                                                                                                                roll_2,
                                                                                                                double_board_states[
                                                                                                                    i])
                for j in range(len(board_state_holder)):
                    if board_state_holder[j] not in final_double_board_states:
                        final_double_board_states.append(board_state_holder[j])

            if len(final_double_board_states) == 0:
                return double_board_states

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
        for i in range(0, 24):
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