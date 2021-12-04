import copy

f = open('input.txt', 'r')
lines = f.readlines()

# Contains string types
numbers_to_draw = lines[0].split(",")


class Board:
    def __init__(self, bingo_board):
        self.board = bingo_board
        # Filled w/ 0s. 1 indicates a position is marked
        self.win_tracker = [[0 for _ in range(5)] for _ in range(5)]
        # keys are the number values on the board : values are its coordinates
        self.coordinates_for_each_number = {}
        self.populate_coordinates()

    def populate_coordinates(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                self.coordinates_for_each_number[self.board[i][j]] = (i, j)

    def get_board(self):
        for row in self.board:
            print(row, '\n')

    def get_win_tracker(self):
        for row in self.win_tracker:
            print(row, '\n')

    def get_coordinate_for_a_number(self, number):
        return self.coordinates_for_each_number[number]

    def does_number_exist_on_board(self, number):
        return True if number in self.coordinates_for_each_number else False

    def check_for_horizontal_win(self, last_coordinate_added):
        """

        :param last_coordinate_added: tuple
        :return: false if not a win or (self.board, winning_row integer) if win
        """
        extracted_row = self.win_tracker[last_coordinate_added[0]]

        if 0 in extracted_row:
            return False
        else:
            unmarked_nums_sum = 0
            for i in range(len(self.board)):
                for j in range(len(self.board)):
                    if self.win_tracker[i][j] != 1:
                        unmarked_nums_sum += int(self.board[i][j])
            # self.get_board()
            # self.get_win_tracker()
            # print(last_coordinate_added)
            return unmarked_nums_sum

    def check_for_vertical_win(self, last_coordinate_added):

        extracted_col = []

        for i in range(len(self.board)):
            extracted_col.append(self.win_tracker[i][last_coordinate_added[1]])

        if 0 in extracted_col:
            return False
        else:
            unmarked_nums_sum = 0
            for i in range(len(self.board)):
                for j in range(len(self.board)):
                    if self.win_tracker[i][j] != 1:
                        unmarked_nums_sum += int(self.board[i][j])
            # self.get_board()
            # self.get_win_tracker()
            # print(last_coordinate_added)
            # print(unmarked_nums_sum)
            return unmarked_nums_sum


    def mark_number_on_board(self, num):
        coordinate_of_num = self.get_coordinate_for_a_number(num)
        self.win_tracker[coordinate_of_num[0]][coordinate_of_num[1]] = 1
        return self.check_for_vertical_win(coordinate_of_num) or self.check_for_horizontal_win(coordinate_of_num)


def build_boards():

    current_board = []

    all_boards = []

    for i in range(2, len(lines)):

        curr = lines[i]

        # If current line is a new line, we have a full board.
        if lines[i] == '\n':
            b = Board(copy.deepcopy(current_board))
            all_boards.append(b)
            current_board.clear()
            continue

        row_as_number_strings = lines[i].split()
        current_board.append(row_as_number_strings)

    return all_boards


all_boards = build_boards()


def play_bingo():

    number_to_draw_index = 0

    while number_to_draw_index < len(numbers_to_draw):
        current_number_at_play = numbers_to_draw[number_to_draw_index]

        for board in all_boards:
            if board.does_number_exist_on_board(current_number_at_play):
                result = board.mark_number_on_board(current_number_at_play)
                if result is not False:
                    # print(all_boards.index(board))
                    # print(current_number_at_play)
                    return int(result) * int(current_number_at_play)

        number_to_draw_index += 1



def play_bingo_2():

    number_to_draw_index = 0
    last_winning_board_object = None
    last_winning_board_result = None
    last_number_at_play = None
    indices_of_winning_boards = set()

    while number_to_draw_index < len(numbers_to_draw):
        current_number_at_play = numbers_to_draw[number_to_draw_index]

        for index in range(len(all_boards)):

            if index in indices_of_winning_boards:
                continue

            if all_boards[index].does_number_exist_on_board(current_number_at_play):
                result = all_boards[index].mark_number_on_board(current_number_at_play)
                if result is not False:
                    indices_of_winning_boards.add(index)
                    last_winning_board_result = int(result)
                    last_number_at_play = int(current_number_at_play)
        number_to_draw_index += 1

    return last_winning_board_result * last_number_at_play

print(play_bingo_2())

