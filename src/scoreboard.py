

class Scoreboard:
    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2
        self.__player1Score = 0
        self.__player2Score = 0

    def get_player1(self):
        return self.__player1

    def get_player2(self):
        return self.__player2

    def get_player1Score(self):
        return self.__player1Score

    def get_player2Score(self):
        return self.__player2Score

    def updateScoreboard(self, c1, c2):
        if c1 == c2:
            self.__player1Score += 0.5
            self.__player2Score += 0.5
            return "Empate"

        if c1 == "P":
            if c2 == "T":
                self.__player2Score += 1
                return self.__player2
            self.__player1Score += 1
            return self.__player1
        if c2 == "P":
            if c1 == "T":
                self.__player1Score += 1
                return self.__player1
            self.__player2Score += 1
            return self.__player2
