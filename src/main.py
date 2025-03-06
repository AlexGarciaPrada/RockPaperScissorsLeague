from SampleBots.rockie import Rockie
from constants import *

demo = Rockie()

for i in range(1,ROUNDS+1):
    print(demo.play(i,FILENAME))