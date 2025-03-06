from SampleBots.rockie import Rockie
from SampleBots.paperly import Paperly


from constants import *
from scoreboard import *


demo = Rockie()
demo2 = Paperly()

scoreboard = Scoreboard(type(demo).__name__,type(demo2).__name__)

for i in range(1,ROUNDS+1):
    scoreboard.updateScoreboard(demo.play(i,FILENAME),demo2.play(i,FILENAME))

scoreboard.printResults()