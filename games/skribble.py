#!/usr/bin/python3

import random
from typing import List
from player import Player
from .game import Game

class Skribble(Game):
    def __init__(self):
        # its a game
        super(Game, self).__init__()
        
        # has the name
        self.name: str = 'Skribble'
        self.description = 'Draw a random word. The others have to guess it.'
        self.player_min = 2
        self.player_max = 10

        # list of words
        self.words: [str] = self.get_wordlist()

        # define running bool
        self.running: bool = len(self.words) > 0
        

    def gameround(self):
        """
        Choose a random word.
        """
        n = random.randint(0, (len(self.words)-1))
        print('Wort: ' + self.words.pop(n))
        print('Noch (%i) Wörter.' % (len(self.words), ))
        
        return 2
