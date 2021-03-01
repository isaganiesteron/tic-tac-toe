import time
import random


class Game:
    def __init__(self, player_1, player_2):
        self.player_1_name = player_1
        self.player_2_name = player_2
        self.game_board = Board()

        # return label[random.randint(0, 2)]

    def start(self):
        print("********Start********\n\n")
        counter = 1
        while True:
            self.game_board.print_board()
            current_player = 1
            current_player_name = self.player_1_name
            if counter % 2 == 0:
                current_player = 2
                current_player_name = self.player_2_name
            while True:
                position_choice = input(f"{current_player_name}'s turn =>  ")
                valid_move = self.game_board.(
                    current_player, position_choice)
                if valid_move:
                    break

            move_result = self.game_board.check_board()
            if move_result:
                winner_name = self.player_1_name
                if move_result == 2:
                    winner_name = self.player_2_name
                print(f"{winner_name} is the WINNER!")
                break
            counter += 1

    def player_move(self, player):
        current_player = self.player_1_name
        if player == 2:
            current_player = self.player_2_name
        choice = input(f"{current_player}'s turn")
        self.game_board.(1, choice)

    def end(self):
        print("Print Results")


class Board:

    def __init__(self):
        self.labels = ["a", "b", "c"]
        self.player = [" X  ", " O  "]  # player 1 is X, player 2 is O
        self.rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def print_board(self):
        row_counter = 0
        print("      row a  | row b  | row c ")
        for row in self.rows:
            col_counter = 0
            col_string = f"row {self.labels[row_counter]}"
            for col in row:
                content = "    "
                if col != 0:
                    content = self.player[col-1]
                if col_counter == 1:
                    col_string += f"|  {content}  |"
                else:
                    col_string += f"  {content}  "
                col_counter += 1
            row_counter += 1
            print(col_string)
        print("\n")

    def (self, player, position):
        if len(position) != 2:
            return False
        else:
            row = self.labels.index(position[0].lower())
            col = self.labels.index(position[1].lower())
            if self.rows[row][col] == 0:
                self.rows[row][col] = player
            else:
                print(f"{position} is already taken. Choose another cell.\n")
                return False
            return True

    def check_board(self):
        # check if there is a winner here

        def check_south(player, row, col):
            for mark in range(2):
                if self.rows[(row+(mark+1))][col] != player:
                    return False
            return True

        def check_east(player, row, col):
            for mark in range(2):
                if self.rows[(row)][col+(mark+1)] != player:
                    return False
            return True

        def check_south_west(player, row, col):
            for mark in range(2):
                if self.rows[(row+(mark+1))][col-((mark+1))] != player:
                    return False
            return True

        def check_south_east(player, row, col):
            for mark in range(2):
                if self.rows[(row+(mark+1))][col+(mark+1)] != player:
                    return False
            return True

        if self.rows[0][0] != 0:  # check S, E, SE
            if check_east(self.rows[0][0], 0, 0):
                return self.rows[0][0]
            elif check_south(self.rows[0][0], 0, 0):
                return self.rows[0][0]
            elif check_south_east(self.rows[0][0], 0, 0):
                return self.rows[0][0]
        elif self.rows[0][1] != 0:  # check S
            if check_south(self.rows[0][1], 0, 1):
                return self.rows[0][1]
        elif self.rows[0][2] != 0:  # check S, SW
            if check_south(self.rows[0][2], 0, 2):
                return self.rows[0][2]
            elif check_south_west(self.rows[0][2], 0, 2):
                return self.rows[0][2]
        elif self.rows[1][0] != 0:  # check E
            if check_east(self.rows[1][0], 1, 0):
                return self.rows[1][0]
        elif self.rows[2][0] != 0:  # check E
            if check_east(self.rows[2][0], 2, 0):
                return self.rows[2][0]
        else:
            return False


first_game = Game("Gani", "Nadine")
first_game.start()