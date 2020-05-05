#!/usr/bin/python3

from typing import Dict
import random
from .game import Game


class Skribble(Game):
    def __init__(self):
        # its a game
        super(Game, self).__init__()

        self.words: [str] = self.get_wordlist()
        self.running: bool = len(self.words) > 0

    def get_info(self, key=None) -> Dict:
        """
        Returns some meta info about the game.
        """
        info: Dict = {
            'name': 'Skribble',
            'description': 'Draw a random word. The others have to guess it.',
            'player_min': 2,
            'player_max': 10
            }
        if key is not None:
            return info[key]
        else:
            return info

    def gameround(self, players):
        """
        Choose a random word.
        """
        n = random.randint(0, (len(self.words)-1))
        self.set_solution(self.words.pop(n))
        print('Wort: ' + self.get_solution())
        print('Noch (%i) Wörter.' % (len(self.words), ))

        return 2
