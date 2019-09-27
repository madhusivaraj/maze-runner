import math
from MapCreator import *
from copy import deepcopy
solvableMap=map_creator(50,0.2)
def euclidean(initial_map): # Computes A* Euclidean
    euclidean_map=deepcopy(initial_map)


    for i in range(len(euclidean_map)): #calculates Euclidean distances
        for j in range(len(euclidean_map)):
            if euclidean_map[i][j] == 0:
                euclidean_map[i][j]= round(math.sqrt(math.pow(i-(len(euclidean_map)-1),2)+(math.pow(j-(len(euclidean_map)-1),2))))

    visited=[] # List of coordinates that have been explored
    path=[] #shortest path
    discovered = [(0,0)] #list of coordinates that have been found but not explored
    previous={}#neighbor of current node that has smallest distance
    distance={(0,0):0, (1,0):1, (0,1):1}#distance travelled for nodes
    current_index=[0,0]
    while True:# for each index, discover it's neighbors, and then make the current index the index with shortest distance

        if (current_index[0]-1) >= 0 and euclidean_map[current_index[0]-1][current_index[1]]!=-1:  # Check to see if top neighbor is in bounds and if its not closed
            if (current_index[0] - 1, current_index[1]) in discovered: #If the node has been discovered by another node, check to see if the distance needs to be updated
                if distance[(current_index[0],current_index[1])]<distance[previous[(current_index[0]-1,current_index[1])]]:
                    previous[(current_index[0]-1,current_index[1])]=(current_index[0],current_index[1])
                    distance[(current_index[0]-1,current_index[1])]=distance[(current_index[0],current_index[1])]+1
            else:
                if (current_index[0] - 1, current_index[1]) not in visited:#if top neighbor has not been discovered and is not in visited, set previous to current node
                    previous[(current_index[0] - 1, current_index[1])] = (current_index[0], current_index[1])
                    distance[(current_index[0] - 1, current_index[1])] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0]-1,current_index[1]))


        if (current_index[1]+1) < len(euclidean_map) and euclidean_map[current_index[0]][current_index[1]+1]!=-1: #  Checks to see if right neighbor is in bounds and if its not closed
            if (current_index[1]+1)==(len(euclidean_map)-1) and (current_index[0])==(len(euclidean_map)-1):  #if goal state reached
                previous[(len(euclidean_map) - 1, len(euclidean_map) - 1)] = (current_index[0], current_index[1]) #sets previous of goal state
                visited.append((current_index[0], current_index[1])) # Adds current index to visited
                visited.append((current_index[0], current_index[1] + 1))  # adds goal index to visited
                backtrack = (len(euclidean_map) - 1, len(euclidean_map) - 1) #start at goal node and backtrack to start node
                while backtrack != (0, 0):
                    path.append(backtrack)
                    backtrack = previous[backtrack]
                path.append((0, 0))
                path.reverse() # Reverses path list so list starts at start index
                for (x,y) in path:
                    euclidean_map[x][y]=-3 # -3 signifies path taken in matrix
                for z in range(len(euclidean_map)):
                    print(euclidean_map[z])
                return len(visited)+len(discovered),len(path), path #Returns visited length + discovered length for part3 and path length for analysis
            if (current_index[0], current_index[1] + 1) in discovered:
                if distance[(current_index[0], current_index[1])] < distance[previous[(current_index[0], current_index[1]+1)]]:
                    previous[(current_index[0] , current_index[1]+1)] = (current_index[0], current_index[1])
                    distance[(current_index[0] , current_index[1]+1)] = distance[(current_index[0], current_index[1])] +1
            else:
                if (current_index[0], current_index[1]+1) not in visited:
                    previous[(current_index[0], current_index[1]+1)] = (current_index[0], current_index[1])
                    distance[(current_index[0], current_index[1]+1)] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0], current_index[1]+1))

        if (current_index[0]+1) < len(euclidean_map) and euclidean_map[current_index[0]+1][current_index[1]]!=-1: # bottom neighbor
            if (current_index[0] + 1) == (len(euclidean_map) - 1) and (current_index[1]) == (len(euclidean_map) - 1):
                previous[(len(euclidean_map) - 1, len(euclidean_map) - 1)] = (current_index[0], current_index[1])
                visited.append((current_index[0], current_index[1]))
                visited.append((current_index[0] + 1, current_index[1]))
                backtrack = (len(euclidean_map) - 1, len(euclidean_map) - 1)
                while backtrack != (0, 0):
                    path.append(backtrack)
                    backtrack = previous[backtrack]
                path.append((0, 0))
                path.reverse()
                for (x, y) in path:
                    euclidean_map[x][y] = -3
                for z in range(len(euclidean_map)):
                    print(euclidean_map[z])

                return len(visited)+len(discovered),len(path),path
            if (current_index[0]+1, current_index[1]) in discovered:
                if distance[(current_index[0], current_index[1])] < distance[previous[(current_index[0]+1, current_index[1])]]:
                    previous[(current_index[0]+1, current_index[1])] = (current_index[0], current_index[1])
                    distance[(current_index[0]+1, current_index[1])] = distance[(current_index[0], current_index[1])] + 1
            else:
                if (current_index[0]+1, current_index[1]) not in visited:
                    previous[(current_index[0]+1, current_index[1])] = (current_index[0], current_index[1])
                    distance[(current_index[0]+1, current_index[1])] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0]+1, current_index[1]))
        if (current_index[1]-1) >=0 and euclidean_map[current_index[0]][current_index[1]-1]!=-1:  # left neighbor
            if (current_index[0], current_index[1]-1) in discovered:
                if distance[(current_index[0], current_index[1])] < distance[previous[(current_index[0], current_index[1]-1)]]:
                    previous[(current_index[0], current_index[1]-1)] = (current_index[0], current_index[1])
                    distance[(current_index[0], current_index[1]-1)] = distance[(current_index[0], current_index[1])] + 1
            else:
                if (current_index[0], current_index[1]-1) not in visited:
                    previous[(current_index[0], current_index[1]-1)] = (current_index[0], current_index[1])
                    distance[(current_index[0], current_index[1]-1)] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0], current_index[1]-1))

        visited.append((current_index[0],current_index[1])) #Adds current_index to visited
        discovered.remove((current_index[0],current_index[1])) #Removes current index from discovered since we visited it.

        if len(discovered) == 0: #Explored all nodes and couldn't find a path.
            return 1,"Failure"
        minimum = euclidean_map[(discovered[0])[0]][(discovered[0])[1]] +distance[discovered[0]] #Sets min distance to first coordinate
        current_index=discovered[0] #if bottom loop fails to assign new current_index, proceed with using the first coordinate in discovered as current_index.
        for (x, y) in discovered:
            if euclidean_map[x][y] + distance[(x, y)] - 1 < minimum:
                current_index=[x,y]




