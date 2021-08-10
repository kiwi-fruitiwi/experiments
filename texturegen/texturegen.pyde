# -*- coding: utf-8 -*-
#
# This creates the transparent texture demoed in Coding Train's Nature of Code 2
# video, 4.4: Particle Systems with Image Textures:
# https://www.youtube.com/watch?v=pUhv2CA0omA
# 
# 2021.08.10
# Author: Kiwi
# I had a lot of trouble with this one because save() doesn't do transparency;
# I resorted to using PGraphics.point(), PGraphics.save()

def setup(): 
    global pg
    size(512, 512)
    
    # Unlike the main drawing surface which is completely opaque, surfaces 
    # created with createGraphics() can have transparency. This makes it possible
    # to draw into a graphics and maintain the alpha channel. By using save() to 
    # write a PNG or TGA file, the transparency of the graphics object will be 
    # honored. 
    pg = createGraphics(width, height)
    

# note the noLoop()! This executes once and could be in setup()
# this draws a circular texture with increasing transparency as r increases
def draw():    
    pg.beginDraw()
    
    cx = width/2
    cy = height/2
    r = width/2
    
    # get the distance of each point (i, j) from the origin, then map this from
    # (0, width/2) (the maximum distance from the center for a circle) to (255, 0)
    # this results in increasing transparency the further away from the center we go 
    for i in range(width):
        for j in range(height):
            d = dist(cx, cy, i, j)
            b = map(d, 0, r, 255, 0)
            pg.stroke(255, 255, 255, b) 
            pg.point(i, j)

    pg.endDraw()
    
    background(0)
    image(pg, 0, 0)
    noLoop()


# save a copy of this image if we push the mouse :3
def mousePressed():    
    pg.save("img_" + str(millis()) + ".png")

    
    
# this was a failed iteration because save() does not handle transparency.
# we moved to PGraphics. this was ported voer from javascript from Daniel Shiffman's
# Nature of Code 2 tutorial.
def draw_transparent():
    size(512, 512)
    pixelDensity(1)
    background(0, 0, 0, 0)
    loadPixels()
    print(len(pixels))
    
    cx = width/2
    cy = height/2    
    r = width/2
    
    for i in range(width):
        for j in range(height):
            d = dist(cx, cy, i, j)
            b = map(d, 0, r, 255, 0)
            # print b
            index = (i + j*width)
            
            pixels[index] = color(255, 255, 255, b)
    updatePixels()
    save("sketch.png")

    # having anything in draw will repeat loop draw, creating a white circle
    # thus we omit the draw function
