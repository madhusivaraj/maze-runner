function [ output ] = map_bfs( map )
% Takes in dim X dim map of 0's and 1's. Uses Breadth First Search to find
% path from start to goal. Returns that path. Returns that path as a list of nodes from start
% node to goal node.

dim = length(map);
goal = [dim,dim];
start = [1,1];
st_prev = start;
visited = {};
parent_list = {};
path = {};
fg = {start}; % fringe
rs = {}; % restricted states
fringed{1} = start; % list of states in order they were added to the fringe
fg_parents{1} = start; % list of parents of each state in fringed list

while length(fg) ~= 0
    st = fg{1}; % state. 2-d vec from fg. newest in fg.
    fg(1) = []; % removes state from fg
    if st == goal
        visited{length(visited)+1} = st;
        parent_list{length(parent_list)+1} = st_prev;
        path{1} = st;
        while sum(path{length(path)}) ~= sum(start)
            for i = 1:length(fringed) % find position of state in visited list
                if fringed{i} == st
                    st_pos = i;
                    break
                end
            end
            st_parent = fg_parents{st_pos};
            path{length(path)+1} = st_parent;
            st_prev = st;
            st = st_parent;
        end
        path2 = path;
        for i = 1:length(path) % this loop reverses order of path list
            path{i} = path2{length(path)-i+1};
        end
        output = path;
        fprintf('Success\n')
        return
    elseif map(st(1),st(2)) == 0
        visited{length(visited)+1} = st;
        parent_list{length(parent_list)+1} = st_prev;
        k = 1;
        while k <= 4 % puts children of state into fringe
            r_step = round(-sin(2*pi*(k-1)/4));
            u_step = round(-cos(2*pi*(k-1)/4));
            ch = st+[u_step, r_step];
            if ch(2) > 0 && ch(2) <= dim % can't be out of x bound
                if ch(1) > 0 && ch(1) <= dim % can't be out of y bound
                    flag = 0;
                    for i = 1:length(rs) % can't be in restricted list
                        if rs{i} == ch
                            flag = 1;
                            break
                        end
                    end
                    for i = 1:length(visited) % can't be previously visited
                        if visited{i} == ch
                            flag = 1;
                            break
                        end
                    end
                    for i = 1:length(fg) % can't be in fringe already
                        if fg{i} == ch
                            flag = 1;
                            break
                        end
                    end
                    if flag == 0
                        fg{length(fg)+1} = ch; %finally adds child to fringe
                        fringed{length(fringed)+1} = ch;
                        fg_parents{length(fg_parents)+1} = st; 
                    end
                end
            end
            k = k+1;
            st_prev = st;
        end
    else % position is wall, ie 1
        rs{length(rs)+1} = st; % adds position to restricted
    end
end

output = visited;
fprintf('Failure\n')
end