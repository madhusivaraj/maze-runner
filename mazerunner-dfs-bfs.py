import map_maker
from dfs_algo import *
from bfs_algo import *
import time


dim = 10# choose dim
p = 0.2# choose p
print('Map\n')
map = map_maker(dim, p) # map_maker generates map

print('DFS\n')
start_time = time.time()
path_dfs = map_dfs(map)
print("--- %s seconds ---" % (time.time() - start_time))
path_map_dfs = map
step = 1

for i in path_dfs[1:len(path_dfs)]:# this loop turns the path list into ASCII map
    tile = path_dfs(i)
    path_map_dfs(tile(1), tile(2)).lvalue = step
    step = step + 1
    path_map_dfs

    print('BFS')
    start_time = time.time()
    path_bfs = map_bfs(map)
    print("--- %s seconds ---" % (time.time() - start_time))
    path_map_bfs = map
    step = 1

    for i in path_bfs[1:len(path_bfs)]:    # this loop turns the path list into ASCII map
        tile = path_bfs(i)
        path_map_bfs(tile(1), tile(2)).lvalue = step
        step = step + 1
        path_map_bfs()