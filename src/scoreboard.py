

class Scoreboard():
    def __init__(self,player1,player2):
        self.player1Score=0
        self.player2Score=0
        self.player1 = player1
        self.player2 = player2

    def updateScoreboard(self,c1,c2):
        if c1 == c2:
            self.player1Score += 0.5
            self.player2Score += 0.5
            return

        if c1 == "P":
            if c2 == "T":
                self.player2Score+=1
                return
            self.player1Score+=1
            return
        if c2 == "P":
            if c1 == "T":
                self.player1Score+=1
                return
            self.player2Score+=1
            return

    def printResults(self):
        print(self.player1 + ": " + str(self.player1Score))
        print(self.player2 + ": " + str(self.player2Score))