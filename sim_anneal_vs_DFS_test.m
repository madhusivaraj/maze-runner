% Use simulated annealing to create maps which maximize the max fringe size
% in the DFS maze runner algorithm
clear

dim = 100;
p = 0.2;
good_map = 0;
while good_map == 0 % ensures solvable map
    map = map_maker(10,0.2); % initial map
    map_score = map_dfs_outputs_maxfringesize(map);
    good_map = map_score;
end
t = 1;
k = 10;
score_list(1) = map_score;
hardest_map = map;
hardest_map_score = map_score;
score_thresh = 1;

for i=1:2000
    new_map = map;
    dims = size(map);
    good_map = 0;
    while good_map == 0;
        flip_cell = [randi([1 dims(1)]) randi([1 dims(2)])];
        new_map(flip_cell(1),flip_cell(2)) = randi([0 1]);
        new_map(1,1) = 0; % makes start 0
        new_map(dims,dims) = 0; % makes goal 0
        new_map_score = map_dfs_outputs_maxfringesize(new_map);
        good_map = new_map_score;
    end
    if new_map_score > hardest_map_score
        hardest_map = new_map;
        hardest_map_score = new_map_score;
    end
    if new_map_score > map_score
        map = new_map;
        map_score = new_map_score;
    else
        if rand <= exp(-k*(map_score-new_map_score)*t)
            map = new_map;
            map_score = new_map_score;
        end
    end
    score_list(length(score_list)+1) = map_score;
end
plot(score_list)
hardest_map_score
