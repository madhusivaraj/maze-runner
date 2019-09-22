

def manhattan(initial_map): # Computes A* manhattan distance
    manhattan_map=initial_map


    for i in range(len(manhattan_map)):
        for j in range(len(manhattan_map)):
            if manhattan_map[i][j] == 0:
                manhattan_map[i][j]= abs(i-(len(manhattan_map)-1))+abs(j-(len(manhattan_map)-1))
    print(manhattan_map)
    visited=[]
    path=[]
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
                previous[(len(manhattan_map) - 1, len(manhattan_map) - 1)] = (current_index[0], current_index[1])
                visited.append((current_index[0], current_index[1]))
                visited.append((current_index[0], current_index[1] + 1))
                backtrack = (len(manhattan_map) - 1, len(manhattan_map) - 1)
                while backtrack != (0, 0):
                    path.append(backtrack)
                    backtrack = previous[backtrack]
                path.append((0, 0))
                path.reverse()
                return path
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
                previous[(len(manhattan_map) - 1, len(manhattan_map) - 1)] = (current_index[0], current_index[1])
                visited.append((current_index[0], current_index[1]))
                visited.append((current_index[0] + 1, current_index[1]))
                backtrack = (len(manhattan_map) - 1, len(manhattan_map) - 1)
                while backtrack != (0, 0):
                    path.append(backtrack)
                    backtrack = previous[backtrack]
                path.append((0, 0))
                path.reverse()
                return path
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




