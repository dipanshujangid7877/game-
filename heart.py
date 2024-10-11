import math
from turtle import *
def hearta(K):
    return 15*math.sin(K)**3
def heartb(K):
    return 12*math.cos(K)-5*\
    math.cos(2*K)-2*\
    math.cos(3*K)-\
    math.cos(4*K)
speed(1000)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range(5):
        color("#f73487")
        goto(0,0)
        done()



