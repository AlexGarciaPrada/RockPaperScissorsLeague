

class Scoreboard:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.data = {
            player1: [],
            player2: [],
            "Ganador": []
        }

        self.player1data = {"R": 0, "P": 0, "T": 0}
        self.player2data = {"R": 0, "P": 0, "T": 0}

        self.player1Score = 0
        self.player2Score = 0

    def update(self, move1, move2):
        # Reglas de Piedra-Papel-Tijera
        if move1 == move2:
            winner = "Empate"
        elif (move1 == "R" and move2 == "T") or \
             (move1 == "P" and move2 == "R") or \
             (move1 == "T" and move2 == "P"):
            winner = self.player1
            self.player1Score += 1
        else:
            winner = self.player2
            self.player2Score += 1

        # Guardar movimientos y resultado
        self.data[self.player1].append(move1)
        self.data[self.player2].append(move2)
        self.data["Ganador"].append(winner)

        if move1 in self.player1data:
            self.player1data[move1] += 1
        if move2 in self.player2data:
            self.player2data[move2] += 1

        return winner

    def get_history(self):
        return self.data

    def get_statistics(self):
        return {
            "Movimiento": ["R", "P", "T"],
            self.player1: [self.player1data["R"], self.player1data["P"], self.player1data["T"]],
            self.player2: [self.player2data["R"], self.player2data["P"], self.player2data["T"]],
        }




