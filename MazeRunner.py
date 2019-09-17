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
                    map[i][j] = -1  # -1 signifies cell being filled, 0 defines cell being empty
                else:
                    map[i][j] = 0
    return map


def manhattan(initial_map): # Computes A* manhattan distance
    manhattan_map=initial_map


    for i in range(len(manhattan_map)):
        for j in range(len(manhattan_map)):
            if manhattan_map[i][j] == 0:
                manhattan_map[i][j]= abs(i-(len(manhattan_map)-1))+abs(j-(len(manhattan_map)-1))
    print(manhattan_map)
    visited=[]
    discovered = [(0,0)]
    previous={}#neighbor of current node that has smallest distance
    distance={(0,0):0, (1,0):1, (0,1):1}#distance travelled for nodes
    current_index=[0,0]
    while True:# for each index, discover it's neighbors, and then make the current index the index with shortest distance

        if (current_index[0]-1) >= 0 and manhattan_map[current_index[0]-1][current_index[1]]!=-1:  # top neighbor
            if (current_index[0] - 1, current_index[1]) in discovered:
                if distance[(current_index[0],current_index[1])]<distance[previous[(current_index[0]-1,current_index[1])]]:
                    previous[(current_index[0]-1,current_index[1])]=(current_index[0],current_index[1])
                    distance[(current_index[0]-1,current_index[1])]=distance[(current_index[0],current_index[1])]+1
            else:
                if (current_index[0] - 1, current_index[1]) not in visited:
                    previous[(current_index[0] - 1, current_index[1])] = (current_index[0], current_index[1])
                    distance[(current_index[0] - 1, current_index[1])] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0]-1,current_index[1]))


        if (current_index[1]+1) < len(manhattan_map) and manhattan_map[current_index[0]][current_index[1]+1]!=-1: # right neighbor
            if (current_index[1]+1)==(len(manhattan_map)-1) and (current_index[0])==(len(manhattan_map)-1):
                visited.append((current_index[0],current_index[1]))
                visited.append((current_index[0],current_index[1]+1))
                return visited
            if (current_index[0], current_index[1] + 1) in discovered:
                if distance[(current_index[0], current_index[1])] < distance[previous[(current_index[0], current_index[1]+1)]]:
                    previous[(current_index[0] , current_index[1]+1)] = (current_index[0], current_index[1])
                    distance[(current_index[0] , current_index[1]+1)] = distance[(current_index[0], current_index[1])] +1
            else:
                if (current_index[0], current_index[1]+1) not in visited:
                    previous[(current_index[0], current_index[1]+1)] = (current_index[0], current_index[1])
                    distance[(current_index[0], current_index[1]+1)] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0], current_index[1]+1))

        if (current_index[0]+1) < len(manhattan_map) and manhattan_map[current_index[0]+1][current_index[1]]!=-1: # bottom neighbor
            if (current_index[0] + 1) == (len(manhattan_map) - 1) and (current_index[1]) == (len(manhattan_map) - 1):
                visited.append((current_index[0], current_index[1]))
                visited.append((current_index[0]+1, current_index[1]))
                return visited
            if (current_index[0]+1, current_index[1]) in discovered:
                if distance[(current_index[0], current_index[1])] < distance[previous[(current_index[0]+1, current_index[1])]]:
                    previous[(current_index[0]+1, current_index[1])] = (current_index[0], current_index[1])
                    distance[(current_index[0]+1, current_index[1])] = distance[(current_index[0], current_index[1])] + 1
            else:
                if (current_index[0]+1, current_index[1]) not in visited:
                    previous[(current_index[0]+1, current_index[1])] = (current_index[0], current_index[1])
                    distance[(current_index[0]+1, current_index[1])] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0]+1, current_index[1]))
        if (current_index[1]-1) >=0 and manhattan_map[current_index[0]][current_index[1]-1]!=-1:  # left neighbor
            if (current_index[0], current_index[1]-1) in discovered:
                if distance[(current_index[0], current_index[1])] < distance[previous[(current_index[0], current_index[1]-1)]]:
                    previous[(current_index[0], current_index[1]-1)] = (current_index[0], current_index[1])
                    distance[(current_index[0], current_index[1]-1)] = distance[(current_index[0], current_index[1])] + 1
            else:
                if (current_index[0], current_index[1]-1) not in visited:
                    previous[(current_index[0], current_index[1]-1)] = (current_index[0], current_index[1])
                    distance[(current_index[0], current_index[1]-1)] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0], current_index[1]-1))

        visited.append((current_index[0],current_index[1]))
        discovered.remove((current_index[0],current_index[1]))

        if len(discovered) == 0:
            return "Failure"
        minimum = manhattan_map[(discovered[0])[0]][(discovered[0])[1]] +distance[discovered[0]]
        for (x, y) in discovered:
            if manhattan_map[x][y] + distance[(x, y)] - 1 < minimum:
                current_index=[x,y]



print(manhattan(map_creator(dimension_size,p_value)))






