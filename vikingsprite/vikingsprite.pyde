# 2021.09.06
# @author Kiwi
#
# Make your first 2D platformer game IN JUST 10 MINUTES (Godot Game Engine)
# https://www.youtube.com/watch?v=xFEKIWpd0sU

from Sprite import Sprite


# Hajileee's viking sprite https://hajileee.itch.io/hajileees-fantasy-characters-pack
# Idle(7)
# Run(6)
# Jump(5)
# Attack Sequence(9)
# Shield(9)
# Death(9)  
# Canvas Size: 32x32

def setup():
    global sprites, mirror
    
    imageMode(CENTER)
    colorMode(HSB, 360, 100, 100, 100)
    spritesheet = loadImage("viking.png")
    size(700, 300)
    
    delay(100)  # with no delay we never get to see the 1st frame
    
    ichi = spritesheet.get(0, 32, 32, 32)
    ni = spritesheet.get(32, 32, 32, 32)
    san = spritesheet.get(64, 32, 32, 32)
    
    imgs = [ni, ichi, ni, san] 
    sprites = []
    mirror = False
    
    # for i in range(9):
    # sprites.append(Sprite(imgs, 10, 10 + i * 32, random(0.15, 0.25), move=True))
    # sprites.append(sprite_quickman_intro())
    
    for i in range(100):
        # particle = Sprite(imgs, random(width), random(height), random(0.15, 0.25), move=True)
        particle = Sprite(imgs, 0, 0, random(0.15, 0.25), move=True)
        sprites.append(particle)
    

def draw():
    global sprites, mirror    
    background(209, 95, 33)
        
    gravity = PVector(0, 0.1)
    
    # if I press the right arrow, animate walking right. make sure it's mirrored
    # if left arrow, animate walking left
    # pressing spacebar means we switch to the jump animation
    # pressing F switches to jumping + fire or fire animation frame
    
    
    for sprite in sprites:
        sprite.apply_force(gravity)
        sprite.update()
        sprite.edges()
        sprite.animate()
        sprite.show()
    
    
    for sprite in sprites:
        if mirror:
            sprite.show_mirror()
        else:
            sprite.show()
        sprite.animate()


def keyPressed():
    global mirror
    
    if key == 'm':
        mirror = not mirror



# returns a quick man intro sprite sequence
def sprite_quickman_intro():
    spritesheet = loadImage("quickman-intro.png")
    SPRITE_DIMENSIONS = 32
    s = 3 * SPRITE_DIMENSIONS # desired sprite size scale factor
    # put each frame in an imgs list starting with []
    imgs = []
    for i in range(8):
        img = spritesheet.get(i*SPRITE_DIMENSIONS, 0, 32, 32)
        img.resize(s, s)
        imgs.append(img)        
    
        # for i in range(9):
        # sprites.append(Sprite(imgs, 10, 10 + i * 32, random(0.15, 0.25)))
        
    # quick man intro sequence
    intro = Sprite(imgs, width/2 - s/2, height/2 - s/2, 0.15, move=False)
    return intro
    

# this code displays quick man's 8-frame intro animation
def spriteless_quickman_intro():
    spritesheet = loadImage("quickman-intro.png")
    
    # allows us to select the position of the sprite in the sprite sheet
    # as a function of the framecount
    x = frameCount % 8 * 32
    
    # All robot master sprites in mega man 2 are 32x32.
    #
    # The original spritesheet had too little space between each quickman,
    # I edited the file and fixed this.
    #
    # The boss intro sprites start at 0,0 and are 32x32 across 8 sprites
    SPRITE_DIMENSIONS = 32
    img = spritesheet.get(x, 0, 32, 32)
    
    s = SPRITE_DIMENSIONS * 3  # s is the side length of a square sprite
    img.resize(s, s)  # let's make it easier to see and debug    
    
    # center the sprite on the canvas using its side length, s
    image(img, width/2 - s/2, height/2 - s/2)


# our original code without using our Sprite object        
def objectless_sprite():   
    spritesheet = loadImage("quickman-run-shoot-boomerangs.png")
     
    ichi = spritesheet.get(0, 32, 32, 32)
    ni = spritesheet.get(32, 32, 32, 32)
    san = spritesheet.get(64, 32, 32, 32)
    
    imgs = [ni, ichi, ni, san]
    SPRITE_DIMENSIONS = 32
    s = SPRITE_DIMENSIONS * 3  # s is the side length of a square sprite
    for img in imgs:
        img.resize(s, s)  # let's make it easier to see and debug    

    image(imgs[frameCount % len(imgs)], width/2-s/2, height/2 - s/2)
