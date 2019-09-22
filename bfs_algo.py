def map_bfs(map=None):
    # Takes in dim X dim map of 0's and 1's. Uses Breadth First Search to find
    # path from start to goal. Returns that path. Returns that path as a list of nodes from start
    # node to goal node.

    dim = len(map)
    goal = [dim, dim]
    start = [1, 1]
    st_prev = start
    visited = []
    parent_list = []
    path = []
    fg = [start]
    rs = [] # restricted states
    fringed = list()
    fg_parents=list()
    fringed(1).lvalue = start# list of states in order they were added to the fringe
    fg_parents(1).lvalue = start# list of parents of each state in fringed list


    while len(fg) != 0:
        st = fg(1)    # state. 2-d vec from fg. newest in fg.
        fg(1).lvalue = []   # removes state from fg
        if st == goal:
            visited(len(visited) + 1).lvalue = st
            parent_list(len(parent_list) + 1).lvalue = st_prev
            path(1).lvalue = st
            while sum(path(len(path))) != sum(start):
                for i in fringed[1:len(fringed)]:                # find position of state in visited list
                    if fringed(i) == st:
                        st_pos = i
                        break
                        st_parent = fg_parents(st_pos)
                        path(len(path) + 1).lvalue = st_parent
                        st_prev = st
                        st = st_parent
                        path2 = path
                        for i in path[1:length(path)]:                        # this loop reverses order of path list
                            path(i).lvalue = path2(length(path) - i + 1)
                            output = path
                            print('Success')
                            return