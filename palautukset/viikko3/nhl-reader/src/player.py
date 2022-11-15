class Player:
    def __init__(self, name, team, nationality, goals, assists):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.goals = goals
        self.assists = assists
        self.score = goals + assists
    
    def __str__(self):
        string = f"{self.name:20} {self.team:5} {self.goals:2} + {self.assists:2} = {self.score:2}"
        return string
