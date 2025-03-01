import random


class Minesweeper:
    def __init__(self, board_size=8, number_of_mines=10):
        self.board_size = board_size
        self.number_of_mines = number_of_mines
        self.board = [[' ' for _ in range(board_size)] for _ in range(board_size)]
        self.mines = set()
        self.revealed = set()
        self.flagged = set()
        self.game_over = False
        self._initialize_board()

    def _initialize_board(self):
        self._generate_mines()
        self._calculate_numbers()

    def _generate_mines(self):
        while len(self.mines) < self.number_of_mines:
            x, y = random.randint(0, self.board_size - 1), random.randint(0, self.board_size - 1)
            self.mines.add((x, y))

    def _calculate_numbers(self):
        """Calculates the number of mines around each cell."""
        for x in range(self.board_size):
            for y in range(self.board_size):
                if (x, y) in self.mines:
                    continue
                counter = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= x + dx < self.board_size and 0 <= y + dy < self.board_size:
                            if (x + dx, y + dy) in self.mines:
                                counter += 1
                self.board[x][y] = str(counter) if counter > 0 else ' '

    def _is_valid_coordinate(self, x, y):
        """Checks if the coordinates are valid (extracting a complex check into a separate function)."""
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    def print_board(self):
        """Prints the current state of the board."""
        print("  " + " ".join([str(i) for i in range(self.board_size)]))
        for x in range(self.board_size):
            row = [str(x)] + [self.board[x][y] if (x, y) in self.revealed else '?' for y in range(self.board_size)]
            print(" ".join(row))

    def reveal(self, x, y):
        """Reveals a cell."""
        if (x, y) in self.revealed or (x, y) in self.flagged:
            return
        if (x, y) in self.mines:
            self.game_over = True
            return
        self.revealed.add((x, y))
        if self.board[x][y] == ' ':
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.board_size and 0 <= ny < self.board_size:
                        self.reveal(nx, ny)

    def flag(self, x, y):
        if (x, y) not in self.revealed:
            self.flagged ^= {(x, y)}

    def get_input(self):
        """Checks the validity of entered coordinates."""
        while True:
            try:
                x, y = map(int, input("Enter coordinates (x y): ").split())
                if not self._is_valid_coordinate(x, y):
                    print("Invalid coordinates. Try again.")
                    continue
                return x, y
            except ValueError:
                print('Invalid input format. Try again.')
                continue

    def play(self):
        """Main game loop (too long function)."""
        while not self.game_over:
            self.print_board()
            print("1. Reveal a cell")
            print("2. Flag a cell as a mine")
            action = input("Choose an action (1 or 2): ").strip()

            if action == "1":
                self.start_game()
                break
            elif action == "2":
                self.view_statistics()
            else:
                print("Invalid action. Try again.")

            if len(self.revealed) == (self.board_size ** 2 - self.number_of_mines):
                print('Congratulations! You won!')
                self.print_board()
                break

    def start_game(self):
        x, y = self.get_input()
        self.reveal(x, y)
        if self.game_over:
            print('You hit a mine! Game over.')
            self.print_board()

    def view_statistics(self):
        x, y = self.get_input()
        self.flag(x, y)


class GameStatistics:
    def __init__(self):
        self.total_games = self.win_games = self.loss_games = 0

    def update_statistics(self, won):
        """Updates game statistics after a match."""
        self.total_games += 1
        if won:
            self.win_games += 1
        else:
            self.loss_games += 1

    def print_statistics(self):
        """Prints game statistics."""
        print(f"Total games played: {self.total_games}")
        print(f"Games won: {self.win_games}")
        print(f"Games lost: {self.loss_games}")


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
                self.start_game()
            elif choice == "2":
                self.stats.print_statistics()
            elif choice == "3":
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Invalid choice, please try again.")

    def start_game(self):
        """Starts a new game."""
        size = int(input("Choose the board size (e.g., 8 for 8x8): ").strip())
        mines = int(input("Enter the number of mines: ").strip())
        game = Minesweeper(size, mines)
        game.play()
        self.stats.update_statistics(not game.game_over and len(game.revealed) == size**2 - mines)
