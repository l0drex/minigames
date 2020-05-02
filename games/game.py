#!/usr/bin/python3

class Game:
    def __init__(self):
        # name of the game
        self.name: str = 'Game'
        self.description = 'A example game'
        # max and min players
        self.player_max: int = 10
        self.player_min: int = 1
        # False if gameover
        self.running: bool = True
        self.solution: str
        
    def get_name(self):
        return self.name
    
    def get_player_max(self):
        return self.get_player_max

    def get_player_min(self):
        return self.player_min
    
    def get_running(self) -> bool:
        return self.running

    def get_mode(self):
        """
        Returns the gamemode:
            0 if singleplayer
            1 if multiplayer
            2 if both possible
        """
        if self.player_max == 1:
            return 0
        elif self.player_max > 1:
            return 1
        else:
            return 2

    def start(self):
        """
        What happens before the first round?
        """
        print('Willkommen bei ' + self.name)
        print(self.description)
        print()

    def gameround(self) -> int:
        """
        What should happen every round?
        :return: 0 if player lost, 1 if won, 2 if undefined (e.g. all multiplayers)
        """
        self.solution = 'Solution'
        return 1

    def end(self):
        """
        What happens at the end of the game?
        """
        if not self.running:
            print('The solution was: ' + self.solution)
            print('THE END')
            print()

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
