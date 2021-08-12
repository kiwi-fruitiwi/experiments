# visualizes squares in the set N, the natural numbers
class SquaresVis:
    def __init__(self):
        self.arr = [] # our squares array
        self.n = 0
        self.num_squares = 0
        self.cell_size = 64
        self.last_square = None
        
        # checks if we've exceeded the height of the canvas
        self.exceeded_height = False
        
        # this is for checking if we are too far to the right
        # and possibly overlapping some text
        self.width_limit = width - 250
        
        # toggle for if the text becomes too small to display in cells
        self.text_too_small = False


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
            
        stroke(0, 0, 100, 40)
        
        c = self.cell_size
        strokeWeight(1)
        
        # iterate through all elements of our array
        # but wrap around every time we hit a width equal to span
        row = 0
        for i in range(1, self.n+1):
            # highlight cells that represent square numbers
            # this is Cody's algorithm for finding a square lol
            # I wonder if it would be faster to look in a squares array
            if sqrt(i) == int(sqrt(i)):
                fill(0, 0, 100, 100)
                self.last_square = i
            else:
                noFill()
            
            Y_OFFSET = c
            
            # temp variables for rectangle coordinates to reduce clutter
            x = 0
            y = 0
        
            # special case because our array starts at 1, not 0
            # make sure when we reach the width, stay on the same row
            if i % span == 0:
                x = span * c
                y = row * c
                row += 1
            else: 
                x = i % span * c
                y = row * c
                
            rect(x, y + Y_OFFSET, c, c)
            
            if not self.text_too_small:
                # color the squares differently than the non-squares
                if sqrt(i) == int(sqrt(i)):
                    fill(210, 100, 100, 100)
                textSize(14)
                
                # only display i in the cell if our text fits
                # turn this off for all cells if one cell doesn't fit
                if not self.text_too_small and textWidth(str(i)) < c:
                    text(str(i), x, y + Y_OFFSET, c, c)
                else:
                    self.text_too_small = True
                                
                fill(0, 0, 100, 100)
                
            # are we too wide such that our display overlaps the data output?
            if span * c > self.width_limit:
                self.cell_size -= 2
                c = self.cell_size
                Y_OFFSET = c
                   
            # don't let the table grow past the bottom of the canvas
            if row * c > height - 2*c:
                self.exceeded_height = True


        # data display on the top right of the canvas
        textSize(32)
        textAlign(CENTER, CENTER)
        fill(210, 100, 100, 100)
        text("{}".format(self.num_squares), width - 100, 100)
        
        strokeWeight(3)
        fill(0, 0, 100, 100)
        line(width - 140, 130, width - 60, 130)
        text("{}".format(self.n), width - 100, 150)
        text("{:.1f}%".format(self.num_squares/float(self.n)*100), width - 100, 250)
        
        textSize(14)
        text("Last square: {}".format(self.last_square), width - 100, 275)
       
