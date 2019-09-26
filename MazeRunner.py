
from astar_euclidean import *
from astar_manhattan import *
#from bfs import *
from fire_maze import *
from MapCreator import *
from dynamic_algo import *
import random

# dimension_size = int(input())  # Asks the user for the dimension size of the map and converts the string value to an int
# p_value = float(input())  # Asks the user for the probability and converts the string value to a float




print("start")
#print(baseline(map_creator(3,0),0))
print("answer", dynamic(map_creator(5,0),0.5))
print("end")






