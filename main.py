#!/usr/bin/python3

import random
import sys
import os
from typing import List
from player import Player
from games import skribble, hangman


class Main(object):

    def __init__(self):
        self.players: List = []

    def get_game(self):
        print('Suche dir ein Spiel aus:')

        games = [
            skribble.Skribble(),
            hangman.Hangman()
            ]

        i = 0
        for game in games:
            print('[%i] ' % (i, ) + game.get_info(key='name'))
            i += 1
        i = (int)(input('Spiel: '))

        return games[i]

    def set_players(self, player_min: int, player_max: int):
        """
        Returns a list of all players in the game.
        :param player_min: minimum required players
        :param player_max: maximum required players
        """
        players: List = []
        name: str = ' '
        print('Geben Sie bitte n Spielernamen an, wobei %i <= n <= %i'
              % (player_min, player_max))
        while (name != '') and (len(players) < player_max):
            name = input('Spieler {}: '.format(len(players)+1))
            if name != '':
                players.append(Player(name))
            elif len(players) < player_min:
                name = ' '

        print()
        print('{} Spieler registriert.'.format(len(players)))
        print()

        return players

    def get_player_by_name(self, name: str):
        """
        Returns a player object with a specific name.
        """
        for player in self.players:
            if player.get_name() == name:
                return player
        print()

        print('Spieler nicht gefunden.')
        print('Bekannte Spieler:')
        for player in self.players:
            print(player.get_name())

        return None

    def get_winner_round(self, player: Player):
        """
        Returns the winner of a round.
        """
        winner: Player = ''
        inp = ''
        while inp == '' or winner == player:
            inp = input('Wer hat gewonnen? ')
            if inp == '':
                if input('Niemand? (j/n) ') == 'j':
                    winner = None
                    break
            elif inp == player.get_name():
                print('Der hat gespielt.')
                inp = ''
            else:
                winner = self.get_player_by_name(inp)
                if winner is None:
                    inp = ''
                else:
                    break

        return winner

    def get_winner(self):
        """
        Returns the winner of the game.
        """
        winner: str
        points_winner = 0
        for player in self.players:
            for key, value in player.get_stats().items():
                print('{}: {}'.format(key, value))
                if key == 'points':
                    if value >= points_winner:
                        winner = player
            print()

        print('Der Gewinner ist: ' + winner.get_name())
        return winner

    def main(self):
        print('Willkommen bei Lahoumy.')
        game = self.get_game()
        multiplayer: bool = len(self.players) > 1
        print()

        self.players = self.set_players(game.get_info(key='player_min'),
                                        game.get_info(key='player_max'))

        game.start()

        # get random player
        player = self.players[random.randint(0, len(self.players)-1)]

        while game.get_running():
            # game round
            if multiplayer:
                print('Es spielt {}'.format(player.get_name()))

            # play one gameround
            won = game.gameround(self.players)

            # add points to the players
            player.add_round(1)

            if multiplayer:
                player_new: Player = self.get_winner_round(player)
                if player_new is not None:
                    player.add_point(1)
                    player_new.add_point(2)
                    # the winner is the next player
                    player = player_new
            else:
                # in singleplayer
                if won:
                    player.add_point(1)

            if input('Neue Runde ') == 'n':
                break

            print()

        print()

        game.end()
        self.get_winner()


if __name__ == '__main__':
    try:
        Main().main()
    except KeyboardInterrupt:
        print('\nInterrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
