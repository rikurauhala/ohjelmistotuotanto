class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.description = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
            4: "Deuce"
        }

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        elif player_name == self.player2_name:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            if self.m_score1 < 4:
                return self.description[self.m_score1] + "-All"
            return self.description[4]
        if self.m_score1 >= 4 or self.m_score2 >= 4:
            difference = self.m_score1 - self.m_score2
            if difference == 1:
                return "Advantage player1"
            if difference == -1:
                return "Advantage player2"
            if difference >= 2:
                return "Win for player1"
            return "Win for player2" 
        return self.description[self.m_score1] + '-' + self.description[self.m_score2]
