class point:
    def __init__(self, x, y, srs):
        self.x = x
        self.y = y
        self.srs = srs


    def distance_to(self,pt):
        return((self.x - pt.x)**2 + (self.y - pt.y)**2)** 0.5