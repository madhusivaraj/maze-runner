import random
import numpy as np

def baseline(initial_map, q_value):  # Using A* Manhattan to find shortest path and traverses when fire exists.
    manhattan_map = initial_map
    for i in range(len(manhattan_map)): #calculcates Manhattan distances
        for j in range(len(manhattan_map)):
            if manhattan_map[i][j] == 0:
                manhattan_map[i][j] = abs(i - (len(manhattan_map) - 1)) + abs(j - (len(manhattan_map) - 1))
    print(np.matrix(manhattan_map))
    visited = [] # List of coordinates that have been explored
    path = [] #shortest path
    discovered = [(0, 0)] #list of coordinates that have been found but not explored
    previous = {}  # neighbor of current node that has smallest distance
    distance = {(0, 0): 0, (1, 0): 1, (0, 1): 1}  # distance travelled for nodes
    current_index = [0, 0]
    while True:  # for each index, discover it's neighbors, and then make the current index the index with shortest distance

        if (current_index[0] - 1) >= 0 and manhattan_map[current_index[0] - 1][current_index[1]] != -1:  # top neighbor
            if (current_index[0] - 1, current_index[1]) in discovered:
                if distance[(current_index[0], current_index[1])] < distance[previous[(current_index[0] - 1, current_index[1])]]:
                    previous[(current_index[0] - 1, current_index[1])] = (current_index[0], current_index[1])
                    distance[(current_index[0] - 1, current_index[1])] = distance[(current_index[0], current_index[1])] + 1
            else:
                if (current_index[0] - 1, current_index[1]) not in visited:
                    previous[(current_index[0] - 1, current_index[1])] = (current_index[0], current_index[1])
                    distance[(current_index[0] - 1, current_index[1])] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0] - 1, current_index[1]))

        if (current_index[1] + 1) < len(manhattan_map) and manhattan_map[current_index[0]][current_index[1] + 1] != -1:  # right neighbor
            if (current_index[1] + 1) == (len(manhattan_map) - 1) and (current_index[0]) == (len(manhattan_map) - 1):
                previous[(len(manhattan_map) - 1, len(manhattan_map) - 1)] = (current_index[0], current_index[1])
                visited.append((current_index[0], current_index[1]))
                visited.append((current_index[0], current_index[1] + 1))
                backtrack = (len(manhattan_map) - 1, len(manhattan_map) - 1)
                while backtrack != (0, 0):
                    path.append(backtrack)
                    backtrack = previous[backtrack]
                path.append((0, 0))
                path.reverse()

                break
            if (current_index[0], current_index[1] + 1) in discovered:
                if distance[(current_index[0], current_index[1])] < distance[previous[(current_index[0], current_index[1] + 1)]]:
                    previous[(current_index[0], current_index[1] + 1)] = (current_index[0], current_index[1])
                    distance[(current_index[0], current_index[1] + 1)] = distance[(current_index[0], current_index[1])] + 1
            else:
                if (current_index[0], current_index[1] + 1) not in visited:
                    previous[(current_index[0], current_index[1] + 1)] = (current_index[0], current_index[1])
                    distance[(current_index[0], current_index[1] + 1)] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0], current_index[1] + 1))

        if (current_index[0] + 1) < len(manhattan_map) and manhattan_map[current_index[0] + 1][current_index[1]] != -1:  # bottom neighbor
            if (current_index[0] + 1) == (len(manhattan_map) - 1) and (current_index[1]) == (len(manhattan_map) - 1):
                previous[(len(manhattan_map) - 1, len(manhattan_map) - 1)] = (current_index[0], current_index[1])
                visited.append((current_index[0], current_index[1]))
                visited.append((current_index[0] + 1, current_index[1]))
                backtrack = (len(manhattan_map) - 1, len(manhattan_map) - 1)
                while backtrack != (0, 0):
                    path.append(backtrack)
                    backtrack = previous[backtrack]
                path.append((0, 0))
                path.reverse()

                break
            if (current_index[0] + 1, current_index[1]) in discovered:
                if distance[(current_index[0], current_index[1])] < distance[previous[(current_index[0] + 1, current_index[1])]]:
                    previous[(current_index[0] + 1, current_index[1])] = (current_index[0], current_index[1])
                    distance[(current_index[0] + 1, current_index[1])] = distance[(current_index[0], current_index[1])] + 1
            else:
                if (current_index[0] + 1, current_index[1]) not in visited:
                    previous[(current_index[0] + 1, current_index[1])] = (current_index[0], current_index[1])
                    distance[(current_index[0] + 1, current_index[1])] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0] + 1, current_index[1]))
        if (current_index[1] - 1) >= 0 and manhattan_map[current_index[0]][current_index[1] - 1] != -1:  # left neighbor
            if (current_index[0], current_index[1] - 1) in discovered:
                if distance[(current_index[0], current_index[1])] < distance[previous[(current_index[0], current_index[1] - 1)]]:
                    previous[(current_index[0], current_index[1] - 1)] = (current_index[0], current_index[1])
                    distance[(current_index[0], current_index[1] - 1)] = distance[(current_index[0], current_index[1])] + 1
            else:
                if (current_index[0], current_index[1] - 1) not in visited:
                    previous[(current_index[0], current_index[1] - 1)] = (current_index[0], current_index[1])
                    distance[(current_index[0], current_index[1] - 1)] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0], current_index[1] - 1))

        visited.append((current_index[0], current_index[1])) #Adds current_index to visited
        discovered.remove((current_index[0], current_index[1])) #Removes current index from discovered since we visited it.

        if len(discovered) == 0: #Explored all nodes and couldn't find a path.
            return "Failure: Path Blocked"
        minimum = manhattan_map[(discovered[0])[0]][(discovered[0])[1]] + distance[discovered[0]] #Sets min distance to first coordinate
        current_index = discovered[0] #if bottom loop fails to assign new current_index, proceed with using the first coordinate in discovered as current_index.
        for (x, y) in discovered:
            if manhattan_map[x][y] + distance[(x, y)] - 1 < minimum:
                current_index = [x, y]

    manhattan_map[0][len(manhattan_map)-1]=-2 # -2 signifies cell being on fire
    start=path[0]
    fire=(0,len(manhattan_map)-1) #fire starts at rightmost
    for (x,y) in path:
        if manhattan_map[x][y]==-2:
            return "Failure due to fire " #If current index on path is on fire return failure
        if (x,y)==(len(manhattan_map)-1,len(manhattan_map)-1): #if goal state reached
            return "Escaped Fire",path
        for i in range(len(manhattan_map)): #traverses map
            for j in range(len(manhattan_map)):
                if manhattan_map[i][j]!=-2 and manhattan_map[i][j]!=-1: #ignore cells that are already on fire and closed cells
                    numNeighbors=0
                    if i-1>=0 and manhattan_map[i-1][j]==-2: #If top neighbor exists and is on fire, increment numNeighbors on fire.
                        numNeighbors+=1
                    if i + 1 <len(manhattan_map) and manhattan_map[i + 1][j] == -2: #if bot exists and is on fire, increment numNeigbors
                        numNeighbors+=1
                    if j - 1 >= 0 and manhattan_map[i][j-1] == -2: #if left exists and is on fire, increment numNeighbors
                        numNeighbors+=1
                    if j+1<len(manhattan_map) and manhattan_map[i][j+1]==-2: #if right exists and is on fire, increment numNeighbors
                        numNeighbors+=1

                    if random.random()<1-(1-q_value)**numNeighbors: #calculates if cell should be on fire or not.
                        manhattan_map[i][j]=-2







