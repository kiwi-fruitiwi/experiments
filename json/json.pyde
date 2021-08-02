
# Coding Challenge #111: animated sprite
# 2021.08.02
# This was supposed to be for the coding challenge but I had to spend
# an hour experimenting with JSON code instead. Leaving this here for 
# now in case I need JSON query code in py later
import json

class Sprite:
    def __init__(self, animation, x, y, speed):
        self.x = x
        self.y = y
        self.animation = animation
        # self.w = self.animation[0].width
        # self.l = self.animation[0].length
        self.speed = speed
        self.index = 0
    
    
    def show(self):
        #  let index = floor(this.index) % this.len;
        index = floor(self.index) % self.len # ?
        image(self.animation[index], self.x, self.y)
        
    
    # animates from left to right, with a modifier for frame speed
    def animate(self):
        self.index += speed
        self.x += self.speed * 15
        
        if self.x > width:
            self.x = 0  # supposed to be negative self.width


def setup():
    global spritesheet, spritedata
    
    spritesheet = loadImage("revised-quicksheet.png")
    size(700, 300)
    frameRate(8)
    delay(2000)

    '''
    data = loadJSONObject("quicksheet.json")
    frames = data.getJSONArray("frames")
    
    print(frames)
    print(frames.get(0).getString("name"))
    print(frames.get(0).getJSONObject("position"))
    print(frames.size())
    
    test = json.loads(data)
    
    # If you have a Python object, you can convert it into a JSON string 
    # by using the json.dumps() method.
    '''
    with open('horse.json') as file:
        data = file.read()
        result = json.loads(data)
    
    print(len(result["frames"]))
    
    for element in result["frames"]:
        print(element["name"])
        print(element["position"])
        print(element["position"]["x"])
    
    # create custom object "frame" which has name and position
    

def draw():    
    colorMode(HSB, 360, 100, 100, 100)
    background(209, 95, 33)
    
    x = frameCount%8 * 32
    
    # 32x28 is the bounding rectangle?
    # offset = [-5, 0, 2, 1, 0, 0, 0, 2]
    # image(spritesheet.get(x+offset[frameCount%4], 0, 28, 32), 0, 0)
    
    # actually all the sprites are 32x32
    # the original spritesheet had too little space between each quickman
    # I edited the file and fixed this
    # the boss intro sprites start at 0,0 and are 32x32 across 8 sprites
    
    # img = spritesheet.get(x, 0, 32, 32)
    # img.resize(64, 64)
    
    # image(img, 64, 64)
