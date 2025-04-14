from SampleBots.rockie import Rockie
from SampleBots.paperly import Paperly



from constants import *
from referee import *



from battleFileCSV import BattleFileCSV
from src.Scoreboard import Scoreboard



player1 = Rockie()
player2 = Paperly()
player1name= type(player1).__name__
player2name= type(player2).__name__
scoreboard = Scoreboard(player1name, player2name)

csvFile = BattleFileCSV(FILENAME, player1name, player2name,scoreboard)


referee = Referee(player1name,player2name)


for round in range(1,ROUNDS+1):

    move1 = player1.play(round, FILENAME)
    move2 = player2.play(round, FILENAME)
    winner = scoreboard.update(move1, move2)

csvFile.save_history()
csvFile.save_statistics()



