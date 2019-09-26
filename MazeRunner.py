
from astar_euclidean import *
from astar_manhattan import *
from bfs import *
from fire_maze import *
from MapCreator import *
import random

dimension_size = int(input())  # Asks the user for the dimension size of the map and converts the string value to an int
p_value = float(input())  # Asks the user for the probability and converts the string value to a float





print(baseline(map_creator(dimension_size,p_value),0))






