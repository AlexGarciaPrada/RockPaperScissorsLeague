import csv
from constants import *

class BattleFile():
    def __init__(self,FILENAME):
        self.FILENAME = FILENAME

    def startFile(self,player1,player2):

        with open(FILENAME,'w',newline='') as file:
            writer = csv.writer(file,delimiter=',')
            writer.writerow([f"Número de rondas: {ROUNDS}"])

            writer.writerow(["Marcador:"])

            writer.writerow([f"{player1} : 0"])

            writer.writerow([f"{player2} : 0"])

            writer.writerow([])

            writer.writerow([player1, player2, 'Ganador'])
