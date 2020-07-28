import random
from typing import Dict
from .textgame import TextGame


class Skribble(TextGame):

    def __init__(self):
        # its a game
        super(TextGame, self).__init__()

        self.info: Dict = {
            'name': 'Skribble',
            'description': 'Draw a random word. The others have to guess it.',
            'player_min': 2,
            'player_max': 10,
            }

        self.words: [str] = self.get_wordlist()
        self.running: bool = len(self.words) > 0

    def gameround(self, players):
        """
        Choose a random word.
        """
        n = random.randint(0, (len(self.words)-1))
        self.set_solution(self.words.pop(n))
        print('Wort: ' + self.get_solution())
        print('Noch (%i) Wörter.' % (len(self.words), ))

        return 2
