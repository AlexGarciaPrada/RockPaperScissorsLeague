from SampleBots.rockie import Rockie
from SampleBots.paperly import Paperly



from constants import *
from scoreboard import *


from battleFileExcel import BattleFileExcel



player1 = Rockie()
player2 = Paperly()
player1name= type(player1).__name__
player2name= type(player2).__name__
excel = BattleFileExcel(FILENAME, player1name, player2name)

scoreboard = Scoreboard(player1name, player2name)
excel.createExcelHistory()
excel.createScoreboardTable()

for round in range(1,ROUNDS+1):
    print(round)
    firstPlayerMove= player1.play(round, FILENAME)
    secoundPlayerMove= player2.play(round,FILENAME)
    winner= scoreboard.updateScoreboard(firstPlayerMove,secoundPlayerMove)
    excel.updateScoreboardTable(scoreboard.player1Score,scoreboard.player1Score)
    excel.updateExcelHistory(round,firstPlayerMove,secoundPlayerMove,winner)
excel.saveExcel()




