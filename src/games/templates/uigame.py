import curses
from abc import ABC

from .game import Game


class UiGame(Game, ABC):
    def __init__(self):
        # its a game
        super(Game, self).__init__()

        self.words = self.get_wordlist()

    def start(self):
        """
        What happens before the first round?
        """
        print('Welcome to ' + self.get_info('name'))
        print(self.get_info('description'))
        print('\n\n' + input())
        curses.initscr()
        self.win = curses.newwin(20, 60, 0, 0)
        self.win.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        self.win.border(1)
        self.win.nodelay(1)
