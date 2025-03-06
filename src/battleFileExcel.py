import pandas as pd
from openpyxl.reader.excel import load_workbook
from openpyxl.workbook import Workbook

from constants import *



class BattleFileExcel():

    def __init__(self,FILENAME,player1,player2):

        try:
            # Intentar cargar el archivo
            self.file = load_workbook(FILENAME)
        except FileNotFoundError:
            # Si el archivo no existe, crea uno nuevo
            print(f"El archivo {FILENAME} no existe. Creando uno nuevo.")
            self.file = Workbook()
            self.file.save(FILENAME)
            self.file.create_sheet(title='Resultados')

        self.datos = dict()
        self. scoreboard=dict()

        self.player1=player1
        self.FILENAME=FILENAME
        self.player2=player2

        self.datos[player1]=[]
        self.datos[player2]=[]
        self.datos['Ganador']=[]

        self.scoreboard[player1] = [0]
        self.scoreboard[player2] = [0]


    def writeRound(self,c1,c2,winner):
        self.datos[self.player1].append(c1)
        self.datos[self.player2].append(c2)
        self.datos['Ganador'].append(winner)

    def createExcelHistory(self):
        df = pd.DataFrame([self.player1,self.player2,'Ganador'])

        df.to_excel(self.FILENAME, index=False, sheet_name='Resultados')

    def createScoreboardTable(self):
        ws = self.file['Resultados']
        ws.cell(row=SCOREBOARD_ROW,column=SCOREBOARD_COLUMN_INIT,value=self.player1)
        ws.cell(row=SCOREBOARD_ROW, column=SCOREBOARD_COLUMN_INIT+1, value=self.player2)
        ws.cell(row=SCOREBOARD_ROW+1, column=SCOREBOARD_COLUMN_INIT, value=0)
        ws.cell(row=SCOREBOARD_ROW+1, column=SCOREBOARD_COLUMN_INIT+1, value=0)


    def updateScoreboardTable(self,score1,score2):
        ws = self.file['Resultados']
        ws.cell(row=SCOREBOARD_ROW + 1, column=SCOREBOARD_COLUMN_INIT, value=score1)
        ws.cell(row=SCOREBOARD_ROW + 1, column=SCOREBOARD_COLUMN_INIT+1, value=score2)


    def updateExcelHistory(self,round,move1,move2,winner):
        ws = self.file['Resultados']
        ws.cell(row=round + 1, column=PLAYER1_HISTORY_COLUMN, value=move1)
        ws.cell(row=round + 1, column=PLAYER2_HISTORY_COLUMN, value=move2)
        ws.cell(row=round + 1, column=WINNER_HISTORY_COLUMN, value=winner)


    def saveExcel(self):
        self.file.save(FILENAME)