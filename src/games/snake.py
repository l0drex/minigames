import curses
from typing import Dict
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint
from games.templates.uigame import UiGame


class Snake(UiGame):

    def __init__(self):
        # its a game
        super(UiGame, self).__init__()

        self.info: Dict = {
            'name': 'Snake',
            'description': 'Be a snake and eat apples.',
            'player_min': 1,
            'player_max': 1
            }
        self.running: bool = True

    def play(self, players) -> int:
        # Initializing values
        self.key = KEY_RIGHT
        self.score = 0

        # Initial snake co-ordinates
        snake = [[4, 10], [4, 9], [4, 8]]
        # First food co-ordinates
        food = [10, 20]

        # Prints the food
        self.win.addch(food[0], food[1], '*')

        # While Esc key is not pressed
        while (self.key != 27):
            self.win.border(0)
            # Printing 'Score' and
            self.win.addstr(0, 2, 'Score : ' + str(self.score) + ' ')
            # 'SNAKE' strings
            self.win.addstr(0, 27, ' SNAKE ')
            # Increases the speed of Snake as its length increases
            self.win.timeout(int(150 - (len(snake)/5 + len(snake)/10) % 120))

            # Previous key pressed
            prevKey = self.key
            event = self.win.getch()
            self.key = self.key if event == -1 else event

            # If SPACE BAR is pressed, wait for another
            if self.key == ord(' '):
                # one (Pause/Resume)
                self.key = -1
                while self.key != ord(' '):
                    self.key = self.win.getch()
                self.key = prevKey
                continue

            # If an invalid key is pressed
            if self.key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
                self.key = prevKey

            # Calculates the new coordinates of the head of the snake.
            # NOTE: len(snake) increases.
            # This is taken care of later at [1].
            x = snake[0][0]
            y = snake[0][1]
            if self.key == KEY_UP:
                x += -1
            if self.key == KEY_DOWN:
                x += 1
            if self.key == KEY_LEFT:
                y += -1
            if self.key == KEY_RIGHT:
                y += 1
            snake.insert(0, [x, y])

            # Exit if snake crosses the boundaries (Uncomment to enable)
            if(snake[0][0] == 0 or snake[0][0] == 19 or
               snake[0][1] == 0 or snake[0][1] == 59):
                break

            # If snake runs over itself
            if snake[0] in snake[1:]:
                break

            # When snake eats the food
            if snake[0] == food:
                food = []
                self.score += 1
                while food == []:
                    # Calculating next food's coordinates
                    food = [randint(1, 18), randint(1, 58)]
                    if food in snake:
                        food = []
                self.win.addch(food[0], food[1], '*')
            else:
                # [1] If it does not eat the food, length decreases
                last = snake.pop()
                self.win.addch(last[0], last[1], ' ')
            self.win.addch(snake[0][0], snake[0][1], '#')
        self.running = False

    def end(self):
        if not self.running:
            print('\nTHE END')
            curses.endwin()
            print("\nScore - " + str(self.score))
            print("http://bitemelater.in\n")
