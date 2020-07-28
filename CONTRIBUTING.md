# How to write your own game
All games are located in `/src/games/` and are children of the classes in `games/templates`.
These classes provide some useful functions, which also make the games more consistent.
Looking at other games in `/src/games` can be a good starting point, too.

## General stuff
* In the `__init__()`, you can set some global variables for your game.
  * `solution`: The solution for the game round.
  * `guess`: The guess of a player.
  * `running`: If the game is running or over.
* The `get_info()` function is responsible for giving some information about your game:
  * `name`: The name of your game
  * `description`: A short description.
  * `player_min`: The minimum amount of players required to play the game.
  * `player_max`: _You guessed it:_ Similar to min, but maximum players.

## The game
1. `start()` is called. By default, it shows the name of the game and your description.
2. `gameround()` defines what happens in every round.
3. `end()` is used to show something at the end. By default, it shows the solution.
