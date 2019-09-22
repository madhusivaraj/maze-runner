import random

def map_maker(dim=None, p=None):
    # Takes a positive, nonzero integer (dim), and a number between 1 and 0
    # (p).
    # Returns a dim X dim matrix, where the value of each element is randomly
    # decided, with a probability p of being 1, or else being 0. Exceptions are
    # the upper left element, which is the 2, and the lower right, which is 3.
    # The matrix represents a square map. The value 2 is the starting point, 3
    # is the goal point, 0's are open spaces, and 1's are walls.

    for i in map[1:dim]:
        for j in map[1:dim]:
            if random.randint(0,100)<= p:
                map(i, j).lvalue = 1
            else:
                map(i, j).lvalue = 0
                map(1, 1).lvalue = 0
                map(dim, dim).lvalue = 0
                output = map