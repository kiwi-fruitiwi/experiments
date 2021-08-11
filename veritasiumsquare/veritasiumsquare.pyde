# This is based on a visualization in the Veritasium video,
# "The Simplest Math Problem No One Can Solve
# https://youtu.be/094y1Z2wpJg?t=939
#
# The aim is to visualize
# Author: Kiwi Fruitiwi
from SquaresVis import *

def setup():
    global sv
    
    size(700, 700)
    colorMode(HSB, 360, 100, 100, 100)
    
    sv = SquaresVis()
    frameRate(1)

def draw():
    background(209, 95, 33)
    sv.inc()
    sv.show(5)
