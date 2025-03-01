import random

GAME_OVER_TEXT = "You hit a mine! Game over."
win_text = "Congratulations! You won!"
INVALID_INPUT_TEXT = "Invalid input format. Try again."

class minesweeper:
    def __init__(self, size=8, num_mines=10):
        self.s = size
        self.m = num_mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.mines = set()
        self.revealed = set()
        self.flagged = set()
        self.GameOver = False
        self.generate_mines()
        self.calculate_numbers()

    def generate_mines(self):
        """Generates mines on the board."""
        # if 0 <= x + dx < self.s and 0 <= y + dy < self.s:
        #     if (x + dx, y + dy) in self.mines:
        while len(self.mines) < self.m:
            x, y = random.randint(0, self.s - 1), random.randint(0, self.s - 1)
            self.mines.add((x, y))

    def calculate_numbers(self):
        """Calculates the number of mines around each cell."""
        for x in range(self.s):
            for y in range(self.s):
                if (x, y) in self.mines:
                    continue
                cnt = 0  # Погана назва змінної (скорочення, яке важко зрозуміти)
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= x + dx < self.s and 0 <= y + dy < self.s:
                            if (x + dx, y + dy) in self.mines:
                                cnt += 1
                self.board[x][y] = str(cnt) if cnt > 0 else ' '


    def calculateBordSize(self):
        pass


    def print_board(self):
        """Prints the current state of the board."""
        print("  " + " ".join([str(i) for i in range(self.s)]))
        for x in range(self.s):
            row = [str(x)] + [self.board[x][y] if (x, y) in self.revealed else '?' for y in range(self.s)]
            print(" ".join(row))

    def reveal(self, x, y):
        """Reveals a cell."""
        if (x, y) in self.revealed or (x, y) in self.flagged:
            return
        if (x, y) in self.mines:
            self.GameOver = True
            return
        self.revealed.add((x, y))
        if self.board[x][y] == ' ':
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.s and 0 <= ny < self.s:
                        self.reveal(nx, ny)

    def is_valid_coordinate(self, x, y):
        """Checks if the coordinates are valid (extracting a complex check into a separate function)."""
        return 0 <= x < self.s and 0 <= y < self.s

    def flag(self, x, y):
        """Marks a cell as a potential mine."""
        if (x, y) in self.revealed:
            return
        if (x, y) in self.flagged:
            self.flagged.remove((x, y))
        else:
            self.flagged.add((x, y))

    def get_input(self):
        """Checks the validity of entered coordinates."""
        while True:
            try:
                x, y = map(int, input("Enter coordinates (x y): ").split())
                if not self.is_valid_coordinate(x, y):
                    print("Invalid coordinates. Try again.")
                    continue
                return x, y
            except ValueError:
                print(INVALID_INPUT_TEXT)
                continue

    def play(self):
        """Main game loop (too long function)."""
        while not self.GameOver:
            self.print_board()
            print("1. Reveal a cell")
            print("2. Flag a cell as a mine")
            action = input("Choose an action (1 or 2): ").strip()

            if action == "1":
                x, y = self.get_input()
                self.reveal(x, y)
                if self.GameOver:
                    print(GAME_OVER_TEXT)
                    self.print_board()
                    break
            elif action == "2":
                x, y = self.get_input()
                self.flag(x, y)
            else:
                print("Invalid action. Try again.")

            if len(self.revealed) == (self.s ** 2 - self.m):
                print(win_text)
                self.print_board()
                break


class GameStatistics:
    def __init__(self):
        self.total = 0
        self.wins = 0
        self.losses = 0

    def update_statistics(self, won):
        """Updates game statistics after a match."""
        self.total += 1
        if won:
            self.wins += 1
        else:
            self.losses += 1

    def print_statistics(self):
        """Prints game statistics."""
        print(f"Total games played: {self.total}")
        print(f"Games won: {self.wins}")
        print(f"Games lost: {self.losses}")


class GameMenu:
    def __init__(self):
        self.stats = GameStatistics()

    def display_menu(self):
        """Displays the game menu."""
        while True:
            print("\nMenu:")
            print("1. Start a new game")
            print("2. View statistics")
            print("3. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.startGame()
            elif choice == "2":
                self.stats.print_statistics()
            elif choice == "3":
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Invalid choice, please try again.")

    def startGame(self):
        """Starts a new game."""
        size = int(input("Choose the board size (e.g., 8 for 8x8): ").strip())
        mines = int(input("Enter the number of mines: ").strip())
        game = minesweeper(size, mines)
        game.play()
        self.stats.update_statistics(game.GameOver and len(game.revealed) == (game.s ** 2 - game.m))



if __name__ == "__main__":
    menu = GameMenu()
    menu.display_menu()
