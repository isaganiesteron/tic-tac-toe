import random


class Bot:
    def __init__(self, marker):
        self.marker_bot = marker
        self.marker_opponent = 1 if marker == 2 else 2
        self.current_board = []

    def make_move(self, current_board):
        self.current_board = current_board

        def _make_random_move():
            labels = ["a", "b", "c"]
            chosen_cell = ""
            while True:
                random_row = random.randint(0, 2)
                random_col = random.randint(0, 2)
                if self.current_board[random_row][random_col] == 0:
                    chosen_cell = labels[random_row]+labels[random_col]
                    break
            return chosen_cell

        def _check_possible_win(player):
            # check all rows - 3
            possible_wins = []
            row_1 = []
            row_2 = []
            row_3 = []
            col_1 = []
            col_2 = []
            col_3 = []
            diag_1 = []
            diag_2 = []

            if self.current_board[0][0] == player or self.current_board[0][1] == player or self.current_board[0][2] == player:
                if self.current_board[0][0] != player and self.current_board[0][0] == 0:
                    row_1.append("aa")
                if self.current_board[0][1] != player and self.current_board[0][1] == 0:
                    row_1.append("ab")
                if self.current_board[0][2] != player and self.current_board[0][2] == 0:
                    row_1.append("ac")
                if len(row_1) == 1:
                    possible_wins.append(row_1[0])
            if self.current_board[1][0] == player or self.current_board[1][1] == player or self.current_board[1][2] == player:
                if self.current_board[1][0] != player and self.current_board[1][0] == 0:
                    row_2.append("ba")
                if self.current_board[1][1] != player and self.current_board[1][1] == 0:
                    row_2.append("bb")
                if self.current_board[1][2] != player and self.current_board[1][2] == 0:
                    row_2.append("bc")
                if len(row_2) == 1:
                    possible_wins.append(row_2[0])
            if self.current_board[2][0] == player or self.current_board[2][1] == player or self.current_board[2][2] == player:
                if self.current_board[2][0] != player and self.current_board[2][0] == 0:
                    row_3.append("ca")
                if self.current_board[2][1] != player and self.current_board[2][1] == 0:
                    row_3.append("cb")
                if self.current_board[2][2] != player and self.current_board[2][2] == 0:
                    row_3.append("cc")
                if len(row_3) == 1:
                    possible_wins.append(row_3[0])

            # check all cols - 3
            if self.current_board[0][0] == player or self.current_board[1][0] == player or self.current_board[2][0] == player:
                if self.current_board[0][0] != player and self.current_board[0][0] == 0:
                    col_1.append("aa")
                if self.current_board[1][0] != player and self.current_board[1][0] == 0:
                    col_1.append("ba")
                if self.current_board[2][0] != player and self.current_board[2][0] == 0:
                    col_1.append("ca")
                if len(col_1) == 1:
                    possible_wins.append(col_1[0])
            if self.current_board[0][1] == player or self.current_board[1][1] == player or self.current_board[2][1] == player:
                if self.current_board[0][1] != player and self.current_board[0][1] == 0:
                    col_2.append("ab")
                if self.current_board[1][1] != player and self.current_board[1][1] == 0:
                    col_2.append("bb")
                if self.current_board[2][1] != player and self.current_board[2][1] == 0:
                    col_2.append("cb")
                if len(col_2) == 1:
                    possible_wins.append(col_2[0])
            if self.current_board[0][2] == player or self.current_board[1][2] == player or self.current_board[2][2] == player:
                if self.current_board[0][2] != player and self.current_board[0][2] == 0:
                    col_3.append("ac")
                if self.current_board[1][2] != player and self.current_board[1][2] == 0:
                    col_3.append("bc")
                if self.current_board[2][2] != player and self.current_board[2][2] == 0:
                    col_3.append("cc")
                if len(col_3) == 1:
                    possible_wins.append(col_3[0])

            # check diagonals - 2
            if self.current_board[0][0] == player or self.current_board[1][1] == player or self.current_board[2][2] == player:
                if self.current_board[0][0] != player and self.current_board[0][0] == 0:
                    diag_1.append("aa")
                if self.current_board[1][1] != player and self.current_board[1][1] == 0:
                    diag_1.append("bb")
                if self.current_board[2][2] != player and self.current_board[2][2] == 0:
                    diag_1.append("cc")
                if len(diag_1) == 1:
                    possible_wins.append(diag_1[0])
            if self.current_board[2][0] == player or self.current_board[1][1] == player or self.current_board[0][2] == player:
                if self.current_board[2][0] != player and self.current_board[2][0] == 0:
                    diag_2.append("ca")
                if self.current_board[1][1] != player and self.current_board[1][1] == 0:
                    diag_2.append("bb")
                if self.current_board[0][2] != player and self.current_board[0][2] == 0:
                    diag_2.append("ac")
                if len(diag_2) == 1:
                    possible_wins.append(diag_2[0])

            return possible_wins

        defense = _check_possible_win(self.marker_opponent)
        offense = _check_possible_win(self.marker_bot)

        print(f"Defensive moves: {defense} Offensive moves: {offense}")
        if len(defense) > 0:
            return defense[0]
        elif len(offense) > 0:
            return offense[0]
        else:
            return _make_random_move()


class Game:
    def __init__(self, player_1, player_2):
        self.player_1_name = player_1
        self.player_2_name = player_2
        self.robot = None
        if self.player_1_name.lower() == "robot":
            self.robot = Bot(1)
        elif self.player_2_name.lower() == "robot":
            self.robot = Bot(2)
        self.game_board = Board()

    def start(self):
        counter = 1
        while True:
            self.game_board.print_board()
            current_player = 1
            current_player_name = self.player_1_name
            if counter % 2 == 0:
                current_player = 2
                current_player_name = self.player_2_name
            while True:
                if current_player_name.lower() == "robot":
                    position_choice = self.robot.make_move(
                        self.game_board.get_board())
                else:
                    position_choice = input(
                        f"{current_player_name}'s turn =>  ")
                valid_move = self.game_board.place_piece(
                    current_player, position_choice)
                if valid_move:
                    break

            end_result = self.game_board.check_board()
            if end_result:
                self.game_board.print_board()
                if end_result == 3:
                    print("DRAW!")
                else:
                    winner_name = self.player_1_name if end_result == 1 else self.player_2_name
                    print(f"{winner_name} is the WINNER!")
                break
            counter += 1

    def player_move(self, player):
        current_player = self.player_1_name
        if player == 2:
            current_player = self.player_2_name
        choice = input(f"{current_player}'s turn")
        self.game_board.place_piece(1, choice)


class Board:
    def __init__(self):
        self.labels = ["a", "b", "c"]
        self.player = [" X  ", " O  "]  # player 1 is X, player 2 is O
        self.rows = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.moves = 0

    def get_board(self):
        return self.rows

    def print_board(self):
        row_counter = 0
        print("      row a    row b    row c ")
        for row in self.rows:

            if row_counter % 1 == 0 and row_counter != 0:
                print("        -----+--------+----- ")
            col_counter = 0
            col_string = f"row {self.labels[row_counter]}"
            for col in row:
                content = "    "
                if col != 0:
                    content = self.player[col - 1]
                if col_counter == 1:
                    col_string += f"|  {content}  |"
                else:
                    col_string += f"  {content}  "
                col_counter += 1
            row_counter += 1
            print(col_string)
        print("\n")

    def place_piece(self, player, position):
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
            self.moves += 1
            return True

    def check_board(self):
        # check if there is a winner here
        def check_south(player, row, col):
            for mark in range(2):
                if self.rows[(row + (mark + 1))][col] != player:
                    return False
            return True

        def check_east(player, row, col):
            for mark in range(2):
                if self.rows[row][col + (mark + 1)] != player:
                    return False
            return True

        def check_south_west(player, row, col):
            for mark in range(2):
                if self.rows[(row + (mark + 1))][col - (mark + 1)] != player:
                    return False
            return True

        def check_south_east(player, row, col):
            for mark in range(2):
                if self.rows[(row + (mark + 1))][col + (mark + 1)] != player:
                    return False
            return True

        if self.moves == 9:  # no more moves possible
            return 3

        if self.rows[0][0] != 0:  # check S, E, SE
            if check_east(self.rows[0][0], 0, 0):
                return self.rows[0][0]
            elif check_south(self.rows[0][0], 0, 0):
                return self.rows[0][0]
            elif check_south_east(self.rows[0][0], 0, 0):
                return self.rows[0][0]

        if self.rows[0][1] != 0:  # check S
            if check_south(self.rows[0][1], 0, 1):
                return self.rows[0][1]

        if self.rows[0][2] != 0:  # check S, SW
            if check_south(self.rows[0][2], 0, 2):
                return self.rows[0][2]
            elif check_south_west(self.rows[0][2], 0, 2):
                return self.rows[0][2]

        if self.rows[1][0] != 0:  # check E
            if check_east(self.rows[1][0], 1, 0):
                return self.rows[1][0]

        if self.rows[2][0] != 0:  # check E, NE || SW
            if check_east(self.rows[2][0], 2, 0):
                return self.rows[2][0]

        return False


first_game = Game("Gani", "Robot")
first_game.start()
