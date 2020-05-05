# How to write your own game
All games are located in _./games/_ and are children of the class game.
I tried to make the code pretty self explanatory, so you might want to take a closer look at `game.py`.
Looking at other games in that directory can be a good starting point, too.

## General stuff
* In the `__init__()`, you can set some global variables for your game.
  * `solution`: The solution for the a gameround
  * `guess`: The guess of a player.
  * `running`: If the game is running or over. In _Hangman_, running is `false` if all words from the list are guessed.
* The `get_info()` function is responsible for giving some information about your game:
  * `name`: The name of your game
  * `description`: A short description.
  * `player_min`: The minimum amount of players required to play the game.
  * `player_max`: _You guessed it:_ Similar to min, but maximum players.

## The game
1. `start()` is called. By default, it shows the name of the game and your description.
2. `gameround()` defines what happens in every round. In _hangman_ f. e., in every round a player has to guess a word.
This function gets called as long as `running` is true.
3. `end()` is used to show something at the end. By default, it shows the solution and prints the classic _THE END_.
