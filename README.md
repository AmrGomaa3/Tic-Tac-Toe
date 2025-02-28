# **Tic Tac Toe Game**
---
- This is a python script to create a tic tac toe game using OOP principles.
- The script was then turned into an exe file.
- Below is a detailed explanation of how the script was written:
---
### Importing os library
- os library was first imported then used to create a `clear_screen()` function which will be used in the script multiple times.
---
### Creating a Player class
- Created a player class with setter functions for name and symbol.
- Added If function to ensure the player name cannot be blank or duplicate.
- Added If function to ensure player can only choose X or O as symbols.
---
### Creating a Menu class
- Created a menu class with `start_menu()` and `end_menu()` functions.
- Added if functions to ensure user can only choose from the available options in the menu.
---
### Creating a Board class
- Created a board class with initial screen list that contains numbers from 1 to 9.
- Created a `display_screen()` function that shows the board with its elements separated by | to mimic the shape of the tic tac toe board.
- Created an `update_screen()` function to update the board each time a playerplays a turn.
- Created a `reset_screen()` function to return the screen to its original state for when the players decide to reset the game.
---
### Creating a Game class:
- Created a game class that intializes the Player class, the Board class and the Menu class.
- Created functions to take input from players and add them to Player class, Menu class and Board class.
- Created functions to check conditions for draw or win then display the result.
---
- The game is CLI-Based.
- The script effectively uses the `clear_screen()` function to ensure a clean interface when moving from one menu to the other.
- Used auto-py-to-exe to create an exe file.
- Feel free to contact me via email or Linkedin which are available on my profile for inquiries or suggestions!
- Have fun playing the game :)
