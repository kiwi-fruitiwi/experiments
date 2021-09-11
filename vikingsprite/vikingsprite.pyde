# 2021.09.06
# @author Kiwi, project based on:
# Make your first 2D platformer game IN JUST 10 MINUTES (Godot Game Engine)
# https://www.youtube.com/watch?v=xFEKIWpd0sU

# . have idle, run, jump inside sprite.py as spritesheets registered to that action
# add velocity and acceleration 
# activate animations when necessary
#     add attack sequence, shield, and death
#     add looponce functionality for death, attack, shield?
# detect if viking in the air
# 
#
# loop=False doesn't work yet for attack, death, and shield animations
# mirroring doesn't work properly and save state

from Viking import *

def setup():
    global victor, sprites, mirror
    
    imageMode(CENTER)
    colorMode(HSB, 360, 100, 100, 100)
    spritesheet = loadImage("viking.png")
    size(700, 300, P3D)
    
    delay(100)  # with no delay we never get to see the 1st frame
    mirror = False # do we flip the image?    
    victor = Viking(spritesheet, width/2, height/2, 0.1)    
    

def draw():
    global victor, sprites, mirror    
    background(209, 95, 33)
        
    # gravity = PVector(0, 0.1)
    
    # if I press the right arrow, animate walking right. make sure it's mirrored
    # if left arrow, animate walking left
    # pressing spacebar means we switch to the jump animation
    # pressing F switches to jumping + fire or fire animation frame
    
    victor.update()
    victor.animate()
    victor.show()


def keyPressed():
    global victor, mirror
    
    
    # if abs(victor.vel.x) > 0:
    #     victor.set_animation(victor.animation_run)
    # else: # we're not moving
    #     victor.set_animation(victor.animation_idle)
        
    if key == 'a':
        victor.vel = PVector(-4, 0)
        victor.set_animation(victor.animation_run, loop=True)
        victor.facing_right = False
    elif key == 'd':
        victor.vel = PVector(4, 0)
        victor.set_animation(victor.animation_run, loop=True)
        victor.facing_right = True
    # else:
    #     victor.vel = PVector(0, 0)
        
    if key == 'e':
        victor.set_animation(victor.animation_attack, loop=False)
        
    if key == 's':
        victor.set_animation(victor.animation_death, loop=False)


def keyReleased():
    if key == 'a' or key == 'd':
        victor.vel = PVector(0, 0)
        victor.set_animation(victor.animation_idle, loop=True)



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
