from abc import ABC, abstractmethod

class Bot(ABC):
    #Metodos necesarios para la funcionalidad

    def __init__(self,name):
        self.name = name
        self.round_history = {
            'Yo': [],
            'Oponente': [],
            "Ganador": [] #Pondrá V cuando gane el robot, D cuando gane el oponente, E cuando sea empate
        }

        self.my_data = {"R": 0, "P": 0, "T": 0}
        self.opp_data = {"R": 0, "P": 0, "T": 0}

        self.my_score = 0
        self.opp_score = 0

    def updateData(self,c1,c2,winner):

        self.round_history['Yo'].append(c1)
        self.round_history['Oponente'].append(c2)

        if winner == self.name:
            self.round_history['Ganador'].append('V')
            self.my_score += 1

        elif winner == 'Empate':
            self.round_history['Ganador'].append('E')
            self.my_score += 0.5
            self.opp_score = 0.5
        else:
            self.round_history['Ganador'].append('D')
            self.opp_score += 1


        self.my_data[c1]+= 1
        self.opp_data[c2]+= 1

    def getName(self):
        return self.name

    #Metodos abstracto que hay que implementar

    @abstractmethod
    def play(self,counter):
        pass

