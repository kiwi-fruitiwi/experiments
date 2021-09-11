'''
@author Kiwi
@date 2021.09.09

Testing processing's ability to simulate P5.js's textToPoints function
https://p5js.org/reference/#/p5.Font/textToPoints

'''

def setup():
    global fontshape, vertices
    
    colorMode(HSB, 360, 100, 100, 100)
    size(640, 360, P2D)
    
    font = createFont("lucida console", 240)
    fontshape = font.getShape('i') 
    
    vertices = []
    for i in range(fontshape.getVertexCount()):
        vertices.append(fontshape.getVertex(i))
    
    

def draw():  
    global fontshape, vertices      
    background(209, 95, 33)
    
    strokeWeight(1)
    stroke(0, 0, 100)
    
    for v in vertices:
        point(v.x+100, v.y+200)
    
    # beginShape()
    # for v in vertices:
    #     vertex(v.x+100, v.y+200)
    # endShape(CLOSE)
