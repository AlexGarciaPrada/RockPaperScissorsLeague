import signal

import pandas as pd
import os
import csv

from src.Scoreboard import Scoreboard

class BattleFileCSV:
    def __init__(self, filename, player1, player2,scoreboard):
        self.filename = filename
        self.player1 = player1
        self.player2 = player2
        self.scoreboard = scoreboard

        signal.signal(signal.SIGINT, self.handle_exit)
        signal.signal(signal.SIGTERM, self.handle_exit)

        # Siempre crea un archivo nuevo (sobrescribe si ya existe)
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.player1, self.player2, "Ganador"])
        print(f"Archivo sobrescrito: {self.filename}")

    def save_history(self):
        df = pd.DataFrame(self.scoreboard.get_history())
        df.to_csv(self.filename, index=False)
        print(f"Historial guardado en {self.filename}")

    def save_statistics(self):
        stats_df = pd.DataFrame(self.scoreboard.get_statistics())
        stats_filename = os.path.splitext(self.filename)[0] + "_estadisticas.csv"
        stats_df.to_csv(stats_filename, index=False)
        print(f"Estadísticas guardadas en {stats_filename}")


    def handle_exit(self, signum, frame):
        self.save_statistics()
        self.save_history()
        exit(0)
