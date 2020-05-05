#!/usr/bin/python3

from typing import Dict


class Game:
    def __init__(self):
        # False if gameover
        self.solution: str
        self.guess: str
        self.running: bool = not (self.get_guess == self.get_solution)

    def get_info(self, key=None) -> Dict:
        """
        Returns a dictionary with some meta information about the game,
        or you can ask for a specific information

        :name: the name of the game
        :description
        """
        raise NotImplementedError

        info: Dict = {
            'name': 'Game',
            'description': 'An example game.',
            'player_min': 1,
            'player_max': 10
            }
        if key is not None:
            try:
                return info[key]
            except KeyError:
                return None
        else:
            return info

    def get_running(self) -> bool:
        return self.running

    def get_solution(self):
        return self.solution

    def get_guess(self):
        return self.guess

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

    def set_solution(self, solution):
        """
        Defines the solution.
        """
        self.solution = solution

    def start(self):
        """
        What happens before the first round?
        """
        print('Willkommen bei ' + self.get_info('name'))
        print(self.get_info('description'))
        print()

    def gameround(self, players) -> int:
        """
        What should happen every round?
        :param players: list of players in the game
        :return: 0 if player lost, 1 if won,
            2 if undefined (e.g. all multiplayers)
        """

        raise NotImplementedError

        self.set_solution('Solution')

        if len(players) > 1:
            return self.multiplayer(players)
        else:
            return self.singleplayer(players[0])

    def singleplayer(self, players) -> int:
        """
        The singleplayer mode.
        """
        return 1

    def mulitplayer(self, players) -> int:
        """
        The multiplayer mode.
        """
        return 1

    def end(self):
        """
        What happens after the last round?
        """
        if not self.running:
            print('The solution was: ' + self.solution)
            print('THE END')
            print()
