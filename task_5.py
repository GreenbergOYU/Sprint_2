class Results:
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses
class Football(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
    def number_of_wins(self):
        return "Футбольных побед: " + str(self.victories)
    def number_of_draws(self):
        return "Футбольных ничьих:  " + str(self.draws)
    def number_of_losses(self):
        return "Футбольных поражений: " + str(self.losses)
    def total_points(self):
        return "Общее количество очков: " + str(3*self.victories + self.draws)
class Hockey(Results):
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)
    def number_of_wins(self):
        return "Хоккейных побед: " + str(self.victories)
    def number_of_draws(self):
        return "Хоккейных ничьих:  " + str(self.draws)
    def number_of_losses(self):
        return "Хоккейных поражений: " + str(self.losses)
    def total_points(self):
        return "Общее количество очков: " + str(3*self.victories + self.draws)
football_team = Football(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

for team in [football_team, hockey_team]:
    print(team.number_of_wins())
    print(team.number_of_draws())
    print(team.number_of_losses())
    print(team.total_points())