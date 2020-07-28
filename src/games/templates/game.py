from typing import Dict


class Game:
    def __init__(self):
        self.info: Dict = {
            'name': 'Game',
            'description': 'An example game.',
            'player_min': 1,
            'player_max': 10
            }

        self.running: bool = not (self.get_guess == self.get_solution)
        self.solution: str = ''
        self.guess: str = ''
        self.multiplayer_mode = False

    def get_info(self, key=None):
        """
        Returns a dictionary with some meta information about the game,
        or you can ask for a specific information

        :name: the name of the game
        :description
        """

        if key is not None:
            return self.info[key]

        return self.info

    def get_running(self) -> bool:
        return self.running

    def get_solution(self):
        return self.solution

    def get_guess(self):
        return self.guess

    def set_solution(self, solution):
        self.solution = solution

    def get_winner_round(self, player):
        """
        Returns the winner of a round.
        """

        if not self.multiplayer_mode:
            return None

        self.winner = ''
        inp = ''
        while inp == '' or self.winner == player:
            inp = input('Wer hat gewonnen? ')
            if inp == '':
                if input('Niemand? (j/n) ') == 'j':
                    self.winner = None
                    break
            elif inp == player.get_name():
                # if input winner was player in current round
                print('Der hat gespielt.')
                inp = ''
            else:
                # set winner
                # ToDo
                self.winner = self.players[inp]
                if self.winner is None:
                    inp = ''
                else:
                    break

        return self.winner

    def start(self):
        """
        What happens before the first round?
        """
        print('Willkommen bei ' + self.get_info('name'))
        print(self.get_info('description'))
        print()

    def play(self, players) -> int:
        """
        What should happen every round?
        :param players: list of players in the game
        :return: 0 if player lost, 1 if won,
            2 if undefined (e.g. all multiplayers)
        """

        self.multiplayer_mode = players is not None

        self.solution = 'Solution'

        if len(players) > 1:
            return self.multiplayer(players)
        else:
            return self.singleplayer(players[0])

    def singleplayer(self, players) -> int:
        """
        The singleplayer mode.
        """
        raise NotImplementedError

    def multiplayer(self, players) -> int:
        """
        The multiplayer mode.
        """
        raise NotImplementedError

    def end(self):
        """
        What happens after the last round?
        """
        if not self.running:
            print('The solution was: ' + self.solution)
            print('THE END')
            print()
