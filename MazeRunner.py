import random  # to calculate p values

dimension_size = int(input())  # Asks the user for the dimension size of the map and converts the string value to an int
p_value = float(input())  # Asks the user for the probability and converts the string value to a float


def map_creator(dim, p):  # Function that returns initial map
    map = [[None for x in range(dim)] for y in range(dim)]  # Initializes array
    for i in range(dim):  # Traverses array, ignoring the goal and start state.
        for j in range(dim):
            if (i == 0 and j == 0) or (i == (dim - 1) and j == (dim - 1)):
                continue
            else:
                if random.random() < p:
                    map[i][j] = 1  # 1 signifies cell being filled, 0 signifies cell being empty
                else:
                    map[i][j] = 0

    return map
