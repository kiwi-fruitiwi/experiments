class Viking():
    def __init__(self, spritesheet, x, y, animation_speed): 
        self.pos = PVector(x, y)
        self.vel = PVector()
        self.acc = PVector(0, 0)        
        self.speed = animation_speed
        self.max_speed = 4
        self.spritesheet = spritesheet
        self.target_size = 256
        
        self.facing_right = True
        self.finished = False # has our animation reached its last frame once?
        self.loop = True
        
        # add all the animations in the sprite sheet
        # Hajileee's viking sprite 
        # https://hajileee.itch.io/hajileees-fantasy-characters-pack
        #     Idle(7)
        #     Run(6)
        #     Jump(5)
        #     Attack Sequence(9)
        #     Shield(9)
        #     Death(9)  
        #     Canvas Size: 32x32
        #
        # this guy's collision box is more of an ellipse        
        self.animation_idle = self.spritesheet_select(self.spritesheet, 0, 7)
        self.animation_run = self.spritesheet_select(self.spritesheet, 1, 6)
        self.animation_jump = self.spritesheet_select(self.spritesheet, 2, 5)
        self.animation_attack = self.spritesheet_select(self.spritesheet, 3, 9)
        self.animation_shield = self.spritesheet_select(self.spritesheet, 4, 9)
        self.animation_death = self.spritesheet_select(self.spritesheet, 5, 9)
        
        # animation is simply a list of image objects
        # self.animation is the CURRENT animation, which is one out of many
        self.set_animation(self.animation_idle, loop=True)
        self.index = 0
        
        # self.w = self.animation[0].width
        # self.r = self.w
    
    
    def set_animation(self, animation, loop):
        self.animation = animation
        self.frames = len(self.animation)
        self.loop = loop # this boolean controls if we loop the animation or not
        self.index = 0
    
    
    # helper method to retrieve animations from a spritesheet
    # returns a list of images for an action, e.g. idle, run, jump, attack, shield, die
    def spritesheet_select(self, spritesheet, row, frames, w=32, h=32):
        animation = []
        for i in range(frames):
            img = spritesheet.get(32*i, 32*row, w, h)
            img.resize(self.target_size, self.target_size)
            animation.append(img)
        return animation
            
    
    # updates the velocity and position
    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(self.max_speed) # limit to our maximum speed
        self.pos.add(self.vel)
        self.acc.mult(0)
    
    
    def apply_force(self, force):
        # F=ma, but assume m=1 so F=a
        self.acc.add(force)
        
    
    # advances the frames
    def animate(self):
        ANIMATION_RATE = self.speed        
        self.index += self.speed
    
    
    # check to make sure our sprite is constrained within the edges
    # of the canvas. invert velocity if it goes past an edge to give a
    # "bounce" effect. 
    # TODO: finish this? 
    def edges(self):
        if self.pos.x + self.r <= 0:
            self.vel.x *= -1
            self.pos.x = self.r
            print("bounce!")
        
    
    # 
    def show(self):   
        index = floor(self.index) % self.frames
        frame = self.animation[index]
        
        if self.facing_right:
            image(frame, self.pos.x, self.pos.y)
        else:
            pushMatrix()
            translate(self.pos.x, self.pos.y);
            scale(-1, 1)
            image(frame, 0, 0)
            popMatrix()
                
                    
     
    
    # shows the sprite facing the opposite direction horizontally
    # def show_mirror(self):
        
    #     index = floor(self.index) % self.frames
        
    #     frame = self.animation[index]        
    #     pushMatrix()
    #     translate(self.pos.x, self.pos.y);
    #     scale(-1, 1)
    #     image(frame, 0, 0)
    #     popMatrix()
