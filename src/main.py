from SampleBots.rockie import Rockie
from SampleBots.paperly import Paperly



from constants import *
from referee import *



from battleFileCSV import BattleFileCSV
from src.Scoreboard import Scoreboard



player1 = Rockie("El rocas")
player2 = Paperly("El sin papeles")

player1name= player1.getName()
player2name= player2.getName()
scoreboard = Scoreboard(player1name, player2name)

csvFile = BattleFileCSV(FILENAME, player1name, player2name,scoreboard)


referee = Referee(player1name,player2name)


for round in range(1,ROUNDS+1):

    move1 = player1.play(round)
    move2 = player2.play(round)
    winner = scoreboard.update(move1, move2)
    player1.updateData(move1,move2,winner)
    player2.updateData(move2, move1, winner)

csvFile.save_history()
csvFile.save_statistics()



