# visualizes squares in the set N, the natural numbers
class SquaresVis:
    def __init__(self):
        self.arr = []
        self.n = 0
        self.num_squares = 0
        self.cell_size = 8


    def inc(self):
        self.n += 1
        if sqrt(self.n) == int(sqrt(self.n)):
            # we found a square!
            self.num_squares += 1
        self.arr.append(self.n)
    
    
    # decrement the array, but if we're already at 1, don't do anything
    def dec(self):
        if self.n != 1:
            self.n -= 1
            self.arr.pop(len(self.arr)-1)
        

    # span is how wide we go before we wrap around
    def show(self, span):
        mono = createFont("terminus.ttf", 16);
        textFont(mono);
            
        stroke(0, 0, 100, 20)
        
        c = self.cell_size
        
        # iterate through all elements of our array
        # but wrap around every time we hit a width equal to span
        row = 0
        for i in range(1, self.n+1):
            # highlight cells that represent square numbers
            # this is Cody's algorithm for finding a square lol
            # I wonder if it would be faster to look in a squares array
            if sqrt(i) == int(sqrt(i)):
                fill(0, 0, 100, 60)
            else:
                noFill()
            
            # special case because our array starts at 1, not 0
            # make sure when we reach the width, stay on the same row  
            if i % span == 0:
                rect(span * c, row * c, c, c)
                row += 1
            else: rect(i % span * c, row * c, c, c)
        
        text("{} / {}".format(self.num_squares, self.n), width - 100, 30)
