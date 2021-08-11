# visualizes squares in the set N, the natural numbers
class SquaresVis:
    def __init__(self):
        self.arr = []
        self.n = 0


    def inc(self):
        self.n += 1
        self.arr.append(self.n)
        

    # span is how wide we go before we wrap around
    def show(self, span):
        
        print(self.arr)
