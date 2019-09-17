import math

def map_dfs(map=None):
    dim = len(map)
    goal = [dim, dim]
    start = [1, 1]
    path = list()
    fg = {start}
    rs = list()

    while len(fg) != 0:
        st = fg[len(fg)]  # state. 2-d vec from fg. newest in fg.
        fg[len(fg)] = [] # removes state from fg
        if st == goal:
            path[len(path) + 1] = st
            print('Success')
            output = path
        elif map(st(1), st(2)) == 0:
            path[len(path) + 1] = st
            k = 1
            while k <= 4:            # puts children of state into fringe
                r_step = round(-1*math.sin(2 * math.pi * (k - 1) / 4))
                u_step = round(-1*math.cos(2 * math.pi * (k - 1) / 4))
                ch = []
                ch = st + [u_step, r_step]
                if ch[1] > 0 and ch[1] <= dim:# can't be out of x bound
                    if ch[0] > 0 and ch[0] <= dim:  # can't be out of y bound
                        flag = 0
                        for i in rs[1:len(rs)]: # can't be in restricted list
                            if rs(i) == ch:
                                flag = 1
                                break
                        for i in path[1:len(path)]: # can't be previously visited
                            if path(i) == ch:
                                flag = 1
                                break
                        if flag == 0:
                            fg(len(fg) + 1).lvalue = ch # finally adds child to fringe
                k = k + 1
        else:  # position is wall, ie 1
            rs[len(rs) + 1] = st # adds position to restricted
    output = path
    print('Failure')