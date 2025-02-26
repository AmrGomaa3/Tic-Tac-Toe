# import library
import os

# creating a clear screen function
def clear_screen():
    os.system('cls')

# creating a player class
class Player:
    
    def __init__ (self):
        self.name = ""
        self.symbol = ""
    def set_name(self):
        while True:
            player_name = input('Enter your name: ')
            if not player_name.strip():
                input('Player name cannot be empty\nPress any key to continue...')
                clear_screen()
            else:
                break
        self.name = player_name

    def set_symbol(self):
        while True:
            player_symbol = input('Choose a symbol (X or O): ')
            if player_symbol.upper() == 'X' or player_symbol.upper() == 'O':
                self.symbol = player_symbol.upper()
                break
            else:
                input('Invalid input. Please choose X or O.\nPress any key to continue...')
                clear_screen()

# creating a menu class
class Menu:
    
    def start_menu(self):
        while True:
            choice = input('Welcome to Tic-TacToe!\n 1. Start Game\n 2. Quit Game\n')
            if choice == '1' or choice == '2':
                return choice
                break
            else:
                input('Invalid input\nPress any key to continue...')
                clear_screen()

    def end_menu(self):
        while True:
            choice = input('1. Restart Game\n2. Quit Game\n')
            if choice == '1' or choice == '2':
                return choice
                break
            else:
                input('Invalid input\nPress any key to continue...')
                clear_screen()

# creating a board class
class Board:

    def __init__ (self):
        self.screen = [str(i) for i in range (1, 10)]

    def display_screen(self):
        for i in range(0, 9, 3):
            print(' | '.join(self.screen[i:i+3]))
            if i < 6:
                print('-' * 9)

    def update_screen(self, player, symbol):
        while True:
            move = input(f'{player}, Choose a spot: ')
            screen = [str(i) for i in range (1, 10)]
            if move in screen:
                if self.screen[int(move) - 1] == 'X' or self.screen[int(move) - 1] == 'O':
                    input('Please choose an open spot\nPress any key to continue...')
                else:
                    self.screen[int(move) - 1] = symbol
                    break
            else:
                input('Invalid input\nPress any key to continue...')

    def reset_screen(self):
        self.screen = [str(i) for i in range (1, 10)]

# creating a game class
class Game:
    def __init__(self):
        self.menu = Menu()
        self.players = [Player(), Player()]
        self.board = Board()

    def main_menu(self):
        choice = self.menu.start_menu()
        if choice == '1':
            clear_screen()
            self.player_select()
        else:
            pass

    def player_select(self):
        i = 1
        for player in self.players:
            while True:
                print(f'Player {i}')
                player.set_name()
                if self.players[1].name == self.players[0].name:
                    input('Choose a different name\nPress any key to continue...')
                    clear_screen()
                else:
                    break
            if self.players[0].symbol == 'X':
                self.players[1].symbol = 'O'
            elif self.players[0].symbol == 'O':
                self.players[1].symbol = 'X'
            else:
                player.set_symbol()
            print('-' * 20)
            input(f'Player {i} name: {self.players[i-1].name}\nPlayer {i} symbol: {self.players[i-1].symbol}\nPress any key to continue...')
            clear_screen()
            i += 1
        self.start_game()

    def start_game(self):
        i = 0
        while i < 2:
            self.board.display_screen()
            self.board.update_screen(self.players[i].name, self.players[i].symbol)
            i = 1 - i
            if self.check_win() == 'X' or self.check_win() == 'O':
                winner = self.winning_player()
                clear_screen()
                self.board.display_screen()
                input(f'{winner} wins!\nPress any key to continue...')
                clear_screen()
                self.end_menu()
                break
            if self.check_draw():
                clear_screen()
                self.board.display_screen()
                input('Game is a draw! Press any key to continue...')
                clear_screen()
                self.end_menu()
                break
            clear_screen()

    def winning_player(self):
        winner = self.check_win()
        if self.players[0].symbol == winner:
            return self.players[0].name
        else:
            return self.players[1].name

    def check_win(self):
        # check win by rows
        diagonal_1 = 0
        diagonal_2 = 2
        for row in range(0, 7, 3):
            if self.board.screen[row] == self.board.screen[row+1] == self.board.screen[row+2]:
                return self.board.screen[row]
        for column in range(0, 3):
            if self.board.screen[column] == self.board.screen[column+3] == self.board.screen[column+6]:
                return self.board.screen[column]
        if self.board.screen[diagonal_1] == self.board.screen[diagonal_1+4] == self.board.screen[diagonal_1+8]:
            return self.board.screen[diagonal_1]
        if self.board.screen[diagonal_2] == self.board.screen[diagonal_2+2] == self.board.screen[diagonal_2+4]:
            return self.board.screen[diagonal_2]
            
    def check_draw(self):
        for i in self.board.screen:
            if i != 'X' and i != 'O':
                return False
        return True

    def end_menu(self):
        choice = self.menu.end_menu()
        if choice == '1':
            clear_screen()
            self.game_reset()
        else:
            pass

    def game_reset(self):
        self.board.reset_screen()
        self.players = [Player(), Player()]
        self.player_select()

game = Game()
game.main_menu()