% This script makes a map, runs DFS and BFS to find a path through the map,
% and out puts ASCII representations of the map and the two paths.

clear
dim = 10; % choose dim
p = 0.2; % choose p
fprintf('Map\n')
map = map_maker(dim,p) % function map_maker generates map

fprintf('DFS\n')
tic
path_dfs = map_dfs(map);
toc % reports DFS runtime
path_map_dfs = map;
step = 1;

for i = 1:length(path_dfs) % this loop turns the path list into ASCII map
    tile = path_dfs{i};
    path_map_dfs(tile(1),tile(2)) = step;
    step = step + 1;
end
path_map_dfs

fprintf('BFS\n')
tic
path_bfs = map_bfs(map);
toc % reports BFS runtime
path_map_bfs = map;
step = 1;

for i = 1:length(path_bfs) % this loop turns the path list into ASCII map
    tile = path_bfs{i};
    path_map_bfs(tile(1),tile(2)) = step;
    step = step + 1;
end
path_map_bfs

