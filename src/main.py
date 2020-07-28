#!/usr/bin/python3

import random
from typing import List
from player import Player
from games.examples import snake, hangman, skribble


class Main(object):

    def __init__(self):
        self.players: List = []
        self.games = [
            skribble.Skribble(),
            hangman.Hangman(),
            snake.Snake()
        ]

    def set_game(self):
        print('Select a game:')
        i = 0
        for game in self.games:
            print('[%i] ' % (i, ) + game.get_info(key='name'))
            i += 1
        i = int(input('Spiel: '))

        return self.games[i]

    def set_players(self, player_min: int, player_max: int):
        """
        Returns a list of all players in the game.
        :param player_min: minimum required players
        :param player_max: maximum required players
        """
        name: str = ' '
        print('Please give between %i and %i names for your players'
              % (player_min, player_max))
        while (name != '') and (len(self.players) < player_max):
            name = input('Players {}: '.format(len(self.players)+1))
            if name != '':
                self.players.append(Player(name))
            elif len(self.players) < player_min:
                name = ' '

        print()
        print('{} players registered.'.format(len(self.players)))
        print()

    def get_winner(self):
        """
        Returns the self.winner of the game.
        """
        winner: Player = Player('none')
        points_winner = 0
        for player in self.players:
            for key, value in player.get_stats().items():
                print('{}: {}'.format(key, value))
                if key == 'points':
                    if value >= points_winner:
                        winner = player
            print()

        print('The winner is: ' + winner.get_name())
        return winner

    def main(self):
        print('Welcome to Lahoumy.')
        game = self.set_game()
        multiplayer: bool = len(self.players) > 1
        print()

        self.set_players(game.get_info(key='player_min'),
                         game.get_info(key='player_max'))

        game.start()

        # get random player
        player = self.players[random.randint(0, len(self.players)-1)]

        while game.get_running():
            # game round
            if multiplayer:
                print('{} plays now'.format(player.get_name()))

            # play one game round
            won = game.play(self.players)

            # add points to the players
            player.add_round(1)

            if multiplayer:
                player_new: Player = game.get_winner_round(player)
                if player_new is not None:
                    player.add_point(1)
                    player_new.add_point(2)
                    # the self.winner is the next player
                    player = player_new
            else:
                # in single player
                if won:
                    player.add_point(1)

            if input('New round? (y)') != 'y':
                break

            print()

        print()

        game.end()
        self.get_winner()


if __name__ == '__main__':
    Main().main()
