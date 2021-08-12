# This is based on a visualization in the Veritasium video,
# "The Simplest Math Problem No One Can Solve
# https://youtu.be/094y1Z2wpJg?t=939
#
# The aim is to visualize
# Author: Kiwi Fruitiwi
from SquaresVis import *

def setup():
    global sv, span, exceeded
    
    size(1200, 800)
    colorMode(HSB, 360, 100, 100, 100)
    
    sv = SquaresVis()
    span = 10
    noSmooth()
    

def draw():
    global sv, span, exceeded
    background(209, 95, 33)
    
    INCREMENT = 1
    
    for i in range(INCREMENT):
        sv.inc()
    sv.show(span)
    
    if sv.exceeded_height:
        span += 1
        sv.exceeded_height = False
    

def mousePressed():
    noLoop()    
    
# def mouseWheel(event): 
#     global span
    
#     e = event.getCount()
    
#     if e == 1:
#         span += 1
    
#     if e == -1:
#         span -= 1


# def keyPressed():
#     if key == "a":
#         sv.dec()
#     if key == "d":
#         sv.inc()
