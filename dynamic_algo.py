import numpy as np
import math

def dynamic(initial_map, q): # Computes A* euclidean distance
    dynamic_map=initial_map

    visited=[]
    discovered = [(0,0)]
    path=[]
    previous={}#neighbor of current node that has smallest distance
    distance={(0,0):0, (1,0):1, (0,1):1}#distance travelled for nodes
    current_index=[0,0]

    while True:# for each index, discover it's neighbors, and then make the current index the index with shortest distance

        if (current_index[1]+1) < len(dynamic_map) and dynamic_map[current_index[0]][current_index[1]+1]!=-1: # right neighbor
            if dynamic_map[current_index[0]][current_index[1] + 1] == -2:
                pass
            elif dynamic_map[current_index[0]][current_index[1]+1]!=-2:
                previous[(len(dynamic_map) - 1, len(dynamic_map) - 1)] = (current_index[0], current_index[1])
                visited.append((current_index[0], current_index[1]))
                visited.append((current_index[0] + 1, current_index[1]))
                backtrack = (len(dynamic_map) - 1, len(dynamic_map) - 1)
                while backtrack != (0, 0):
                    path.append(backtrack)
                    backtrack = previous[backtrack]
                path.append((0, 0))
                path.reverse()

                return visited, path

        if (current_index[0]+1) < len(dynamic_map) and dynamic_map[current_index[0]+1][current_index[1]]!=-1: # bottom neighbor
            if dynamic_map[current_index[0]+1][current_index[1]] == -2:
                pass
            elif dynamic_map[current_index[0]+1][current_index[1]]!=-2:
                previous[(len(dynamic_map) - 1, len(dynamic_map) - 1)] = (current_index[0], current_index[1])
                visited.append((current_index[0], current_index[1]))
                visited.append((current_index[0] + 1, current_index[1]))
                backtrack = (len(dynamic_map) - 1, len(dynamic_map) - 1)
                while backtrack != (0, 0):
                    path.append(backtrack)
                    backtrack = previous[backtrack]
                path.append((0, 0))
                path.reverse()

                return visited, path

        if (current_index[0]-1) < len(dynamic_map) and dynamic_map[current_index[0]-1][current_index[1]]!=-1: # top neighbor
            if dynamic_map[current_index[0]-1][current_index[1]] == -2:
                pass
            elif dynamic_map[current_index[0]-1][current_index[1]]!=-2:
                previous[(current_index[0]-1,current_index[1])]=(current_index[0],current_index[1])
                visited.append((current_index[0], current_index[1]))
                backtrack = (len(dynamic_map) - 1, len(dynamic_map) - 1)
                while backtrack != (0, 0):
                    path.append(backtrack)
                    backtrack = previous[backtrack]
                path.append((0, 0))
                path.reverse()

                return visited, path

        if (current_index[1] - 1) < len(dynamic_map) and dynamic_map[current_index[0]][current_index[1]-1] != -1: # left neighbor
            if dynamic_map[current_index[0]][current_index[1]-1] == -2:
                pass
            elif dynamic_map[current_index[0]][current_index[1]-1] != -2:
                previous[(current_index[0], current_index[1]-1)] = (current_index[0], current_index[1])
                visited.append((current_index[0], current_index[1]))
                backtrack = (len(dynamic_map) - 1, len(dynamic_map) - 1)
                while backtrack != (0, 0):
                    path.append(backtrack)
                    backtrack = previous[backtrack]
                path.append((0, 0))
                path.reverse()

                return visited, path

        visited.append((current_index[0],current_index[1]))
        discovered.remove((current_index[0],current_index[1]))

