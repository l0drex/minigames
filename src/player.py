class Player:
    def __init__(self, name: str):
        self.name = name
        self.points = 0
        self.rounds = 0

    def add_point(self, plus: int):
        self.points += plus

    def add_round(self, plus: int):
        self.rounds += plus

    def get_name(self):
        return self.name

    def get_stats(self):
        return {'name': self.name,
                'points': self.points,
                'rounds': self.rounds}
