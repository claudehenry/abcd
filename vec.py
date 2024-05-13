
class Vec:
    def __init__(self, *vs):
        self.vs = vs

    def __add__(self, other):
        self.vs = [a * b for (a, b) in self.vs.zip(other.vs)]
