import numpy as np
import math
import random

def dynamic(initial_map, q_value): # Computes A* euclidean distance
    print("INIT", initial_map)
    dynamic_map=initial_map
    visited=[(0,0)]
    discovered = [(0,0)]
    path=[]
    previous={}#neighbor of current node that has smallest distance
    distance={(0,0):0, (1,0):1, (0,1):1}#distance travelled for nodes
    current_index=[0,0]

    while current_index != (len(initial_map)-1,len(initial_map)-1):# for each index, discover it's neighbors, and then make the current index the index with shortest distance
        if (current_index[1]+1) < len(dynamic_map) and dynamic_map[current_index[0]][current_index[1]+1]!=-1: # right neighbor
            print("RIGHT")
            if dynamic_map[current_index[0]][current_index[1] + 1] == -2:
                pass
            elif dynamic_map[current_index[0]][current_index[1]+1]!=-2:
                print("curright", current_index)
                print("pr", previous)
                print("pre-nosejob", visited)
                print("ummm", (current_index[0], current_index[1]+1))
                visited.append((current_index[0], current_index[1]+1))
                print("post-nosejob", visited)
                dynamic_map[current_index[0]][current_index[1] + 1] == -1
                path=visited
                visited.reverse()
                current_index = visited[0]
                visited.sort()
                print("visited", visited)
        if (current_index[0]+1) < len(dynamic_map) and dynamic_map[current_index[0]+1][current_index[1]]!=-1: # bottom neighbor
            print("BOTTOM")
            print("curr inde", current_index)
            if dynamic_map[current_index[0]+1][current_index[1]] == -2:
                pass
            elif dynamic_map[current_index[0]+1][current_index[1]]!=-2:
                previous[(current_index[0]+1, current_index[1])] = (current_index[0], current_index[1])
                print("curr", current_index, "prv", previous)
                print("OG",visited)
                print("ummm", (current_index[0]+1, current_index[1]))
                visited.append((current_index[0]+1, current_index[1]))
                print("post-nosejob", visited)
                #dynamic_map[current_index[0]+1][current_index[1]] == -1
                print("visited1", visited)
                visited.reverse()
                current_index = visited[0]
                visited.sort()
                print("visited2", visited)
        if dynamic_map[current_index[0] - 1][current_index[1]] == -1 and dynamic_map[current_index[0]][current_index[1] + 1] == -1:
            if (current_index[0] - 1) < len(dynamic_map) and dynamic_map[current_index[0] - 1][current_index[1]] != -1:  # top neighbor
                print("TOP")
                if dynamic_map[current_index[0] - 1][current_index[1]] == -2:
                    pass
                elif dynamic_map[current_index[0] - 1][current_index[1]] != -2:
                    previous[(current_index[0] - 1, current_index[1])] = (current_index[0], current_index[1])
                    print("curr", current_index, "prv", previous)
                    print("OG", visited)
                    print("ummm", (current_index[0] - 1, current_index[1]))
                    visited.append((current_index[0] - 1, current_index[1]))
                    print("post-nosejob", visited)
                    # dynamic_map[current_index[0]+1][current_index[1]] == -1
                    print("visited1", visited)
                    visited.reverse()
                    current_index = visited[0]
                    visited.sort()
                    print("visited2", visited)
            if (current_index[1] - 1) < len(dynamic_map) and dynamic_map[current_index[0]][current_index[1] - 1] != -1:  # left neighbor
                print("LEFT")
                if dynamic_map[current_index[0]][current_index[1] - 1] == -2:
                    pass
                elif dynamic_map[current_index[0]][current_index[1] - 1] != -2:
                    print("curright", current_index)
                    print("pr", previous)
                    print("pre-nosejob", visited)
                    print("ummm", (current_index[0], current_index[1] - 1))
                    visited.append((current_index[0], current_index[1] - 1))
                    print("post-nosejob", visited)
                    dynamic_map[current_index[0]][current_index[1] - 1] == -1
                    path = visited
                    visited.reverse()
                    current_index = visited[0]
                    visited.sort()
                    print("visited", visited)

        if (current_index[0],current_index[1]) in discovered:
            discovered.remove((current_index[0],current_index[1]))

    return path
    dynamic_map[0][len(dynamic_map) - 1] = -2  # -2 signifies cell being on fire
    fire = (0, len(dynamic_map) - 1)  # fire starts at rightmost
    for (x, y) in path:
        if dynamic_map[x][y] == -2:
            return "Failure due to fire "  # If current index on path is on fire return failure
        if (x, y) == (len(dynamic_map) - 1, len(dynamic_map) - 1):  # if goal state reached
            return "Escaped Fire", path


        for i in range(len(dynamic_map)):  # traverses map
            for j in range(len(dynamic_map)):
                if dynamic_map[i][j] != -2 and dynamic_map[i][j] != -1:  # ignore cells that are already on fire and closed cells
                    numNeighbors = 0
                    if i - 1 >= 0 and dynamic_map[i - 1][j] == -2:
                        numNeighbors += 1
                    if i + 1 < len(dynamic_map) and dynamic_map[i + 1][j] == -2:
                        numNeighbors += 1
                    if j - 1 >= 0 and dynamic_map[i][j - 1] == -2:
                        numNeighbors += 1
                    if j + 1 < len(dynamic_map) and dynamic_map[i][j + 1] == -2:
                        numNeighbors += 1

                    if random.random() < 1 - (1 - q_value) ** numNeighbors:
                        dynamic_map[i][j] = -2

