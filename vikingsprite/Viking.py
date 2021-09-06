class Viking():
    def __init__(self, animation, x, y, animation_speed): 
        self.pos = PVector(x, y)
        self.vel = PVector()
        self.acc = PVector(0, 0)        
        self.speed = animation_speed
        self.max_speed = 4
        
        # animation is simply a list of image objects
        self.animation = animation 
        self.frames = len(self.animation)          
        self.w = self.animation[0].width
        self.r = self.w
        self.index = 0        
        
    
    # updates the velocity and position
    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(self.max_speed) # limit to our maximum speed
        self.pos.add(self.vel)
        self.acc.mult(0)
    
    
    def apply_force(self, force):
        # F=ma, but assume m=1 so F=a
        self.acc.add(force)
        
    
    def animate(self):
        ANIMATION_RATE = 80 * self.speed        
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
        
    
    def show(self):        
        if self.vel.x < 0:
            self.show_mirror()
        else:
            # our sprite can have a speed below 1!
            # this floor and modulo lets us have decimal indices
            index = floor(self.index) % self.frames        
            frame = self.animation[index]
            image(frame, self.pos.x, self.pos.y)   
     
    
    # shows the sprite facing the opposite direction horizontally
    def show_mirror(self):
        index = floor(self.index) % self.frames
        
        frame = self.animation[index]        
        pushMatrix()
        translate(self.pos.x, self.pos.y);
        scale(-1, 1)
        image(frame, 0, 0)
        popMatrix()
