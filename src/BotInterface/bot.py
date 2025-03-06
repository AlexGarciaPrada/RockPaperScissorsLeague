from abc import ABC, abstractmethod

class Bot(ABC):

    @abstractmethod
    def play(self,counter,fileroute):
        pass
