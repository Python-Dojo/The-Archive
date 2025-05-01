
# Connect four
# https://neopythonic.blogspot.com/2008/10/why-explicit-self-has-to-stay.html
# typical board size
# https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
ROWS = 6
COLUMNS = 7

PLAYER_1 = "🔴"
PLAYER_2 = "🔵"

def print_empty_row():
    print(" " * COLUMNS)



class Connect4:

    def __init__(self) -> None:
        self.board = [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.player = PLAYER_1
        
    def swap_player(self) -> None:
        self.player = PLAYER_1 if self.player == PLAYER_2 else PLAYER_2

    @property
    def columns(self) -> list[list[str]]:
        return [[self.board[i][j]for i in range(ROWS)] for j in range(COLUMNS)] 

    def right_diagonals(self, grid: list[list[str]]) -> list[list[str]]:
        # Add 1 from any 0 coord until
        result = []
        for x in range(ROWS):
            col_index = 0
            result.append([grid[x + y][y] for y in range(COLUMNS) if x+y < ROWS  ])
        for y in range(COLUMNS):
            result.append([grid[x][y + x] for x in range(ROWS) if x+y < COLUMNS ])
        return result
    
    @property
    def diagonals(self) -> list[list[str]]:
        return self.right_diagonals(self.board) + self.right_diagonals([row[::-1] for row in self.board])
        
    def check_victory(self) -> str | None:
        """Return either the winning player or None if no winner currently"""
        print("checking for victory")
        for row in [*self.board, *self.columns, *self.diagonals]:
            # print("".join(row).count(PLAYER_1), "".join(row).count(PLAYER_2))
            if PLAYER_1 * 4 in "".join(row):
                return PLAYER_1
            if PLAYER_2 * 4 in "".join(row):
                return PLAYER_2
        return None
        
    def print_board(self) -> None:
        for row in self.board:
            print("".join(row).replace(" ", "  "))

    def do_user_move(self) -> None:
        move = input(f"Next player please make your move ({self.player}): ")
        while True:
            if move.isdigit() and int(move) in range(1, COLUMNS + 1) and self.make_play(int(move) - 1):
                return
            move = input("Not a valid move please pick another: ")
            
        
    def make_play(self, column:int) -> bool:
        for i in range(ROWS):
            if (self.board[i][column] != ' '):
                if i == 0:
                    # Column is full so move is invalid
                    # |     X    | <- Top of board cannot make move above
                    # |     OX   |
                    return False
                self.board[i-1][column] = self.player
                return True
        else:
            # nothing in this row yet
            self.board[ROWS-1][column] = self.player
        return True

    def play(self) -> None:
        """Game loop"""
        while not (victor := self.check_victory()):
            self.do_user_move()
            self.swap_player()
            self.print_board()
        print(f"Player {victor} wins!")

if __name__ == "__main__":
    game = Connect4()
    game.play()

