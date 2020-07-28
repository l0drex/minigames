from typing import List, Dict
from games.templates.textgame import TextGame


class Hangman(TextGame):

    def __init__(self):
        # its a game
        super(TextGame, self).__init__()

        self.info: Dict = {
            'name': 'Hangman',
            'description': 'Guess the word before you run out of guesses.',
            'player_min': 1,
            'player_max': 1
            }

        self.words = self.get_wordlist()
        self.running: bool = len(self.words) > 0

    def play(self, players) -> int:
        """
        What should happen every round?
        """

        # count mistakes
        tries_left: int = 11

        # create guessed word
        guessed: List = []

        # letters guessed
        self.letters: List = []

        # define the solution
        if len(players) > 1:
            self.multiplayer(players)
        else:
            self.singleplayer(players[0])

        # let the player guess
        for _ in self.solution:
            guessed.append('_')

        end = 1
        while not(''.join(guessed) == self.solution):
            print(''.join(guessed))

            # choose a letter
            inp: chr = input('Letter: ').casefold()
            if inp == '':
                if input('Cancel? ') == 'j':
                    end = 0
            elif inp in self.letters:
                print('You already tried that.')
            elif inp in self.solution:
                print('Correct!')
                self.letters.append(inp)
                for i in range(len(self.solution)):
                    if inp == self.solution[i]:
                        guessed[i] = inp
            else:
                print('Sadly not.')
                self.letters.append(inp)
                tries_left -= 1
                print('%i tries left.' % (tries_left, ))

                if tries_left <= 0:
                    end = 0

        if end == 0:
            print('The solution was ' + self.get_solution())

        return end

    def singleplayer(self, players):
        # generate a random word
        self.set_solution(self.get_word().casefold())

    def multiplayer(self, player):
        # let the player choose a word
        self.set_solution(input('Word to guess: '))
