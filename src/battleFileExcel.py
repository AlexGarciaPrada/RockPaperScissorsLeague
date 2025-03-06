import pandas as pd




class BattleFileExcel():

    def __init__(self,FILENAME,player1,player2):
        self.datos = dict()
        self.player1=player1
        self.FILENAME=FILENAME

        self.player2=player2
        self.datos[player1]=[]
        self.datos[player2]=[]
        self.datos['Ganador']=[]


    def writeRound(self,c1,c2,winner):
        self.datos[self.player1].append(c1)
        self.datos[self.player2].append(c2)
        self.datos['Ganador'].append(winner)

    def makeExcel(self):
        df = pd.DataFrame(self.datos)  # Convertimos el diccionario en un DataFrame
        print(df)  # Muestra la tabla
        df.to_excel(self.FILENAME, index=False, sheet_name="Resultados")