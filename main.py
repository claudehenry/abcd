from mat import Mat
from vec import Vec

ma = Mat()
mb = Mat(Vec(1, 0, 0, 0), Vec(0, 1, 0, 0), Vec(0, 0, 1, 0), Vec(0, 0, 0, 1))

assert ma == mb
