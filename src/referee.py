

class Referee:
    def __init__(self, player1, player2):
        self.__player1 = player1
        self.__player2 = player2


    def selectWinner(self, c1, c2):
        if c1 == c2:
            return "Empate"

        if c1 == "P":
            if c2 == "T":
                return self.__player2
            return self.__player1
        if c2 == "P":
            if c1 == "T":
                return self.__player1
            return self.__player2
