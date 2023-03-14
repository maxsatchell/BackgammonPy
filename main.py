import ast
import copy
import random
import tensorflow as tf
import keras
from enum import Enum
from deepdiff import DeepDiff
import pandas as pd
import numpy as np
from model import BackgammonModel
from colours import Colours
from player import Player
from board import Board
from location import Location
from keras.layers import Dense



# Testing the crossover

def roll_dice():
    dice = random.randint(1, 6)
    return dice


class Program:

    # There may be wrong games before 3265 in the game history before the bug fixes
    #4361
    def run_one_game(games):
        number_of_wins_black = 0
        number_of_wins_white = 0
        tf.random.set_seed(1234)#Might be a problem with seeding changing the model
        backgammonModel_1_AI_2 = BackgammonModel(56, 3, 10, 32)
        loadedModel_1_AI_2 = tf.keras.models.load_model(r'C:\Users\Max\PycharmProjects\BackgammonPy\Models\model_1_AI_2.h5')
        backgammonModel_1_AI_2.update_internal_model(loadedModel_1_AI_2)
        tf.random.set_seed(4321)
        backgammonModel_2_5_AI_2 = BackgammonModel(56, 3, 10, 32)
        loadedModel_2_5_AI_2 = tf.keras.models.load_model(r'C:\Users\Max\PycharmProjects\BackgammonPy\Models\model_2_5_AI_2.h5')
        backgammonModel_2_5_AI_2.update_internal_model(loadedModel_2_5_AI_2)
        #training_data = Program.read_history_from_file()
        #backgammonModel_2_5_AI_2.train(training_data)
        #backgammonModel_2_5_AI_2.save(r'C:\Users\Max\PycharmProjects\BackgammonPy\Models\model_2_5_AI_2.h5')
        #backgammonModel_0_AI_2.save(r'C:\Users\Max\PycharmProjects\BackgammonPy\Models\model_0_AI_2.h5')
        for i in range(0,games):
            game_board = Board(Board.starting_board())
            player1 = Player(Colours.WHITE, "White", game_board)
            player2 = Player(Colours.BLACK, "Black", game_board)
            game = Game(player1, player2, player2, game_board)
            board_history = []
            Program.board_outputter(game.board)
            starting_board = copy.deepcopy(game.board)
            while not game.board.game_finished():
                # Left model is white, right model is black
                game.run_neural_network(backgammonModel_2_5_AI_2,backgammonModel_1_AI_2)
                board_history.append(game.board)

            if game.board.locations[50].number == 15:
                number_of_wins_black+=1
                df = starting_board.convert_to_pd_with_winner(1)
                Program.write_history_to_file(1,board_history,df)
                print("Game is finished the winner is Black  The game number is "+  str(i))
            else:
                number_of_wins_white+=1
                df = starting_board.convert_to_pd_with_winner(-1)
                Program.write_history_to_file(-1,board_history,df)
                print("Game is finished the winner is White  The game number is "+  str(i))
        print("The number of wins for black is " + str(number_of_wins_black))
        print("The number of wins for white is " + str(number_of_wins_white))
        print("The number of games played was " + str(games))
    def write_history_to_file(winner,board_history,df):
        for move in board_history:
            check = move.convert_to_pd_with_winner(winner)
            df = df.append(check)
        df.to_csv('game_history_1_AI_2_vs_2.5_AI_2.csv', mode='a', index=False, header=False)

    def read_history_from_file():
        df2 = pd.read_csv("overall_game_history.csv")
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

    def run_neural_network(self,model_0,model_1):
        if self.board.game_finished():
            return
        roll1 = roll_dice()
        roll2 = roll_dice()
        print(self.current_player.name + "Rolled " + str(roll1) + " " + str(roll2))
        # The end game checker is not working and there may be issues with min black and white for later also white issues
        if len(self.board.valid_moves(self.current_player.colour, roll1)) == 0 and \
                len(self.board.valid_moves(self.current_player.colour, roll2)) == 0:
            print("No valid moves for " + self.current_player.name +" the rolls where " + str(roll1) +" "+ str(roll2))
            Game.player_swapper(self)
            return

        copy_board = copy.deepcopy(self.board)
        copy_current_player = copy.deepcopy(self.current_player)

        board_states = copy_board.generate_valid_board_states_after_both_moves(copy_current_player.colour, roll1,roll2)
        #for i in board_states:
            #Program.board_outputter(i)
        #if self.current_player.colour.value == nnplayer:
        randomiser = random.randint(0,100)
        if randomiser > 97:
            if len(board_states) == 1:
                selected_move = board_states[0]
                self.board = selected_move
                Program.board_outputter(self.board)
                Game.player_swapper(self)
                return
            rando_board = random.randint(0,(len(board_states) -1))
            selected_move = board_states[rando_board]
            self.board = selected_move
            Program.board_outputter(self.board)
            Game.player_swapper(self)
            return

        max_value = 0
        best_move = board_states[0]
        for i in range(0,len(board_states)):
            # get a copy of a board
            if copy_current_player.colour.value == 1:#choose if white or black
                #value = model.predict(np.array(board_states[i].convert_to_pd()).reshape(-1, 56))[0][1]
                value = model_1.predict(board_states[i].convert_to_pd(), 1)
            else:
                #value = model.predict(np.array(board_states[i].convert_to_pd()).reshape(-1, 56))[0][2]
                value = model_0.predict(board_states[i].convert_to_pd(), 2)#choose if white or black
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
    Program.run_one_game(5)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
