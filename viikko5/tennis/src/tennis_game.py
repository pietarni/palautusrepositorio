class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return f"{self.SCORE_NAMES[self.m_score1]}-All" if self.m_score1 < 3 else "Deuce"

        if self.m_score1 >= 4 or self.m_score2 >= 4:
            score_diff = self.m_score1 - self.m_score2
            if score_diff == 1:
                return "Advantage player1"
            elif score_diff == -1:
                return "Advantage player2"
            elif score_diff >= 2:
                return "Win for player1"
            else:
                return "Win for player2"

        return f"{self.SCORE_NAMES[self.m_score1]}-{self.SCORE_NAMES[self.m_score2]}"
