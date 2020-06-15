import random
from .game import Game


class TextGame(Game):
    def __init__(self):
        # its a game
        super(Game, self).__init__()

        self.words = self.get_wordlist()

    def get_wordlist(self) -> [str]:
        """
        Returns a list of words saved in ./src/words.txt.
        """
        with open('./games/src/words.txt', 'r') as file:
            words = file.readlines()
        words = [s.strip() for s in words]

        print('{} Wörter gefunden.'.format(len(words)))
        print()

        return words

    def get_word(self) -> str:
        """
        Returns a random word from the wordlist
        return: random word
        """
        n = random.randint(0, (len(self.words)-1))
        return self.words.pop(n)
