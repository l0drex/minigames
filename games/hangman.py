#!/usr/bin/python3

import random
from .game import Game

class Hangman(Game):
    def __init__(self):
        # its a game
        super(Game, self).__init__()

        self.name = 'Hangman'
        self.description = 'Guess the word before you run out of guesses.'
        self.player_min = 1
        self.player_max = 1

        self.words = self.get_wordlist()
        self.running: bool = len(self.words) > 0
        self.solution: str
        
    def get_name(self):
        return self.name

    def gameround(self) -> int:
        """
        What should happen every round?
        """
        # generate a random word
        n = random.randint(0, (len(self.words)-1))
        self.solution = self.words.pop(n).casefold()

        # count mistakes
        tries_left: int = 11

        # create guessed word
        guessed: List = []

        # letters guessed
        letters: List = []

        for letter in self.solution:
            guessed.append('_')

        while not(''.join(guessed) == self.solution):
            print(''.join(guessed))

            inp: str = input('Buchstabe: ').casefold()
            if inp == '':
                if input('Abbrechen? ') == 'j':
                    return 0
            elif inp in letters:
                print('Das hast du schon versucht.')
            elif inp in self.solution:
                print('Korrekt!')
                letters.append(inp)
                for i in range(len(self.solution)):
                    if inp == self.solution[i]:
                        guessed[i] = inp
            else:
                print('Leider falsch.')
                letters.append(inp)
                tries_left -= 1
                print('%i Versuche übrig.' % (tries_left, ))

                if tries_left <= 0:
                    return 0


        return 1

