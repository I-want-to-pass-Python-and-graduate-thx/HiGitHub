#hw5
# (1) need to design at least three functions
# (2) must use dictionary to store the board in Minesweeper 
# (3) store the current draw cards of players in Blackjack
import random

class Minesweeper: #define a name of a set of functions
    def __init__(self): #初始條件，宣告時會自動執行，括號裡是要沿用的名字
        self.board = [[' ' for _ in range(9)] for _ in range(9)] #初始格子
        self.mines = set() #初始地雷
        self.help_message = "Enter the column followed by the row (ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f). Type 'help' to show this message again."
        self.first_turn = True
        self.generate_mines()
        self.display_help()
        
    
    def display_help(self):
        print(self.help_message)

    def generate_mines(self):
        self.mines = set(random.sample(range(81), 10))

    def print_board(self):
        print("    a   b   c   d   e   f   g   h   i  ")
        print("  +---+---+---+---+---+---+---+---+---+")
        for i, row in enumerate(self.board, 1):
            print(f"{i} |   |   |   |   |   |   |   |   |   |")
            print("  +---+---+---+---+---+---+---+---+---+")

    def count_mines(self, row, col):
        count = 0
        for i in range(row-1, row+2):
            for j in range(col-1, col+2):
                if (0 <= i < 9) and (0 <= j < 9) and (i*9 + j) in self.mines:
                    count += 1
        return count

    def unfold_cell(self, cell):
        col = ord(cell[0]) - ord('a')
        row = int(cell[1]) - 1
        if self.board[row][col] != ' ':
            print("Cell already unfolded.")
            return False
        if self.first_turn:
            self.generate_mines()
            while (row*9 + col) in self.mines:
                self.generate_mines()
            self.first_turn = False
        if row*9 + col in self.mines:
            print("Game over! You stepped on a mine.")
            self.board[row][col] = 'X'
            self.print_board()
            return True
        else:
            count = self.count_mines(row, col)
            self.board[row][col] = '0' if count == 0 else str(count)
        return False

    def flag_cell(self, cell):
        col = ord(cell[0]) - ord('a')
        row = int(cell[1]) - 1
        if self.board[row][col] == ' ':
            self.board[row][col] = 'F'
        elif self.board[row][col] == 'F':
            self.board[row][col] = ' '


# Example usage:
game = Minesweeper()
game.print_board()
while True:
    user_input = input("Enter the cell (10 mines left): ")
    if user_input.lower() == 'help':
        game.display_help()
    elif user_input[-1].lower() == 'f':
        game.flag_cell(user_input[:-1])
        game.print_board()
    else:
        if game.unfold_cell(user_input):
            break
        game.print_board()