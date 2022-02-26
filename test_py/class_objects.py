class point:
    def __init__(self, x, y, srs):
        self.x = x
        self.y = y
        self.srs = srs


    def distance_to(self,pt):
        return((self.x - pt.x)**2 + (self.y - pt.y)**2)** 0.5

    def __str__(self):
        str = "Point({0:.5f}, {1:.5f})".format(self.x, self.y)
        str+= "EPSG code: {0}".format(self.srs)
        return str