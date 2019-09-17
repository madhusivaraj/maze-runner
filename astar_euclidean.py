from MazeRunner import *
import math

def euclidean(initial_map): # Computes A* manhattan distance
    euclidean_map=initial_map

    for i in range(len(euclidean_map)):
        for j in range(len(euclidean_map)):
            if euclidean_map[i][j] == 0:
                euclidean_map[i][j]= math.sqrt(math.pow(i-(len(euclidean_map)-1),2)+math.sqrt(math.pow(j-(len(euclidean_map)-1),2)))
    print(euclidean_map)
    visited=[]
    discovered = [(0,0)]
    previous={}#neighbor of current node that has smallest distance
    distance={(0,0):0, (1,0):1, (0,1):1}#distance travelled for nodes
    current_index=[0,0]
    while True:# for each index, discover it's neighbors, and then make the current index the index with shortest distance

        if (current_index[0]-1) >= 0 and euclidean_map[current_index[0]-1][current_index[1]]!=-1:  # top neighbor
            if (current_index[0] - 1, current_index[1]) in discovered:
                if distance[(current_index[0],current_index[1])]<distance[previous[(current_index[0]-1,current_index[1])]]:
                    previous[(current_index[0]-1,current_index[1])]=(current_index[0],current_index[1])
                    distance[(current_index[0]-1,current_index[1])]=distance[(current_index[0],current_index[1])]+1
            else:
                if (current_index[0] - 1, current_index[1]) not in visited:
                    previous[(current_index[0] - 1, current_index[1])] = (current_index[0], current_index[1])
                    distance[(current_index[0] - 1, current_index[1])] = distance[(current_index[0], current_index[1])] + 1
                    discovered.append((current_index[0]-1,current_index[1]))


        if (current_index[1]+1) < len(euclidean_map) and euclidean_map[current_index[0]][current_index[1]+1]!=-1: # right neighbor
            if (current_index[1]+1)==(len(euclidean_map)-1) and (current_index[0])==(len(euclidean_map)-1):
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

        if (current_index[0]+1) < len(euclidean_map) and euclidean_map[current_index[0]+1][current_index[1]]!=-1: # bottom neighbor
            if (current_index[0] + 1) == (len(euclidean_map) - 1) and (current_index[1]) == (len(euclidean_map) - 1):
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

        visited.append((current_index[0],current_index[1]))
        discovered.remove((current_index[0],current_index[1]))

        if len(discovered) == 0:
            return "Failure"
        minimum = euclidean_map[(discovered[0])[0]][(discovered[0])[1]] +distance[discovered[0]]
        for (x, y) in discovered:
            if euclidean_map[x][y] + distance[(x, y)] - 1 < minimum:
                current_index=[x,y]

print(euclidean(map_creator(dimension_size,p_value)))