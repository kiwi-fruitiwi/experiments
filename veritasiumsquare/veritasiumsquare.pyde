# This is based on a visualization in the Veritasium video,
# "The Simplest Math Problem No One Can Solve
# https://youtu.be/094y1Z2wpJg?t=939
#
# The aim is to visualize
# Author: Kiwi Fruitiwi
from SquaresVis import *

def setup():
    global sv, span
    
    size(600, 400)
    colorMode(HSB, 360, 100, 100, 100)
    
    sv = SquaresVis()
    span = 10
    

def draw():
    background(209, 95, 33)
    
    sv.inc()
    sv.show(span)
    
    
def mouseWheel(event): 
    global span
    
    e = event.getCount()
    
    if e == 1:
        span += 1
    
    if e == -1:
        span -= 1


# def keyPressed():
#     if key == "a":
#         sv.dec()
#     if key == "d":
#         sv.inc()
