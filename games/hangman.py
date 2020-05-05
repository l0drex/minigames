#!/usr/bin/python3

from typing import Dict, List
import random
from .game import Game


class Hangman(Game):
    def __init__(self):
        # its a game
        super(Game, self).__init__()

        self.words = self.get_wordlist()
        self.running: bool = len(self.words) > 0

    def get_info(self, key = None) -> Dict:
        """
        Returns some meta info about the game.
        """
        info: Dict = {
            'name': 'Hangman',
            'description': 'Guess the word before you run out of guesses.',
            'player_min': 1,
            'player_max': 1
            }
        if key is not None:
            try:
                return info[key]
            except KeyError:
                return None
        else:
            return info

        return info

    def gameround(self, players) -> int:
        """
        What should happen every round?
        """

        # count mistakes
        self.tries_left: int = 11

        # create guessed word
        self.guessed: List = []

        # letters guessed
        self.letters: List = []

        # define the solution
        if len(players) > 1:
            self.multiplayer()
        else:
            self.singleplayer()

        # let the player guess
        for letter in self.solution:
            self.guessed.append('_')

        while not(''.join(self.guessed) == self.solution):
            print(''.join(self.guessed))

            # choose a letter
            inp: chr = input('Buchstabe: ').casefold()
            if inp == '':
                if input('Abbrechen? ') == 'j':
                    end = 0
            elif inp in self.letters:
                print('Das hast du schon versucht.')
            elif inp in self.solution:
                print('Korrekt!')
                self.letters.append(inp)
                for i in range(len(self.solution)):
                    if inp == self.solution[i]:
                        self.guessed[i] = inp
            else:
                print('Leider falsch.')
                self.letters.append(inp)
                self.tries_left -= 1
                print('%i Versuche übrig.' % (self.tries_left, ))

                if self.tries_left <= 0:
                    end = 0

        end = 1

        if end == 0:
            print('The solution was ' + self.get_solution())

        return end

    def singleplayer(self):
        # generate a random word
        n = random.randint(0, (len(self.words)-1))
        self.set_solution(self.words.pop(n).casefold())

    def multiplayer(self):
        # let the player choose a word
        self.set_solution(input('Zu erratendes Wort: '))
