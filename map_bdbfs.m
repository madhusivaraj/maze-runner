function [ output ] = map_bdbfs( map )
% Takes in dim X dim map of 0's and 1's. Uses Bi-Directional Breadth First Search to find
% path from start to goal. Returns that path. Returns that path as a list of nodes from start
% node to goal node.

dim = length(map);
startF = [1,1];
startB = [dim,dim];
st_prevF = startF;
st_prevB = startB;
visitedF = {};
visitedB = {};
parent_listF = {};
parent_listB = {};
pathF = {};
pathB = {};
fgF = {startF}; % fringe
fgB = {startB};
rs = {}; % restricted states
fringedF{1} = startF; % list of states in order they were added to the fringe
fringedB{1} = startB;
fg_parentsF{1} = startF; % list of parents of each state in fringed list
fg_parentsB{1} = startB;

while length(fgF) ~= 0 && length(fgB) ~= 0
    stF = fgF{1}; % state. 2-d vec from fg. oldest in fg.
    fgF(1) = []; % removes state from fg
    stB = fgB{1}; % state. 2-d vec from fg. oldest in fg.
    fgB(1) = []; % removes state from fg
    for i = 1:length(fgF)
        for j = 1:length(fgB)
            if fgF{i} == fgB{j}
                linkF = fgF{i};
                linkB = fgB{j};
                visitedF{length(visitedF)+1} = stF;
                visitedB{length(visitedB)+1} = stB;
                parent_listF{length(parent_listF)+1} = st_prevF;
                parent_listB{length(parent_listB)+1} = st_prevB;
                stF = linkF;
                stB = linkB; 
                pathF{1} = stF;
                pathB{1} = stB;
                while sum(pathF{length(pathF)}) ~= sum(startF)
                    for i = 1:length(fringedF) % find position of state in visited list
                        if fringedF{i} == stF
                            st_pos = i;
                            break
                        end
                    end
                    st_parentF = fg_parentsF{st_pos};
                    pathF{length(pathF)+1} = st_parentF;
                    st_prevF = stF;
                    stF = st_parentF;
                end
                pathF2 = pathF;
                for i = 1:length(pathF) % this loop reverses order of path list
                    pathF{i} = pathF2{length(pathF)-i+1};
                end
                
                while sum(pathB{length(pathB)}) ~= sum(startB)
                    for i = 1:length(fringedB) % find position of state in visited list
                        if fringedB{i} == stB
                            st_pos = i;
                            break
                        end
                    end
                    st_parentB = fg_parentsB{st_pos};
                    pathB{length(pathB)+1} = st_parentB;
                    st_prevB = stB;
                    stB = st_parentB;
                end
                path = {};
                for i = 1:length(pathF)
                    path{length(path)+1} = pathF{i};
                end
                for i = 2:length(pathB)
                    path{length(path)+1} = pathB{i};
                end
                output=[path];                
                fprintf('Success\n')
                return
            end
        end
    end
%--------------------------------------------------------------------------
% FORWARDS
    if map(stF(1),stF(2)) == 0
        visitedF{length(visitedF)+1} = stF;
        parent_listF{length(parent_listF)+1} = st_prevF;
        k = 1;
        while k <= 4 % puts children of state into fringe
            r_step = round(-sin(2*pi*(k-1)/4));
            u_step = round(-cos(2*pi*(k-1)/4));
            ch = stF+[u_step, r_step];
            if ch(2) > 0 && ch(2) <= dim % can't be out of x bound
                if ch(1) > 0 && ch(1) <= dim % can't be out of y bound
                    flag = 0;
                    for i = 1:length(rs) % can't be in restricted list
                        if rs{i} == ch
                            flag = 1;
                            break
                        end
                    end
                    for i = 1:length(visitedF) % can't be previously visited
                        if visitedF{i} == ch
                            flag = 1;
                            break
                        end
                    end
                    for i = 1:length(fgF) % can't be in fringe already
                        if fgF{i} == ch
                            flag = 1;
                            break
                        end
                    end
                    if flag == 0
                        fgF{length(fgF)+1} = ch; %finally adds child to fringe
                        fringedF{length(fringedF)+1} = ch;
                        fg_parentsF{length(fg_parentsF)+1} = stF; 
                    end
                end
            end
            k = k+1;
            st_prevF = stF;
        end
    else % position is wall, ie 1
        rs{length(rs)+1} = stF; % adds position to restricted
    end
%--------------------------------------------------------------------------
% BACKWARDS
        if map(stB(1),stB(2)) == 0
        visitedB{length(visitedB)+1} = stB;
        parent_listB{length(parent_listB)+1} = st_prevB;
        k = 1;
        while k <= 4 % puts children of state into fringe
            r_step = round(-sin(2*pi*(k-1)/4));
            u_step = round(-cos(2*pi*(k-1)/4));
            ch = stB+[u_step, r_step];
            if ch(2) > 0 && ch(2) <= dim % can't be out of x bound
                if ch(1) > 0 && ch(1) <= dim % can't be out of y bound
                    flag = 0;
                    for i = 1:length(rs) % can't be in restricted list
                        if rs{i} == ch
                            flag = 1;
                            break
                        end
                    end
                    for i = 1:length(visitedB) % can't be previously visited
                        if visitedB{i} == ch
                            flag = 1;
                            break
                        end
                    end
                    for i = 1:length(fgB) % can't be in fringe already
                        if fgB{i} == ch
                            flag = 1;
                            break
                        end
                    end
                    if flag == 0
                        fgB{length(fgB)+1} = ch; %finally adds child to fringe
                        fringedB{length(fringedB)+1} = ch;
                        fg_parentsB{length(fg_parentsB)+1} = stB; 
                    end
                end
            end
            k = k+1;
            st_prevB = stB;
        end
    else % position is wall, ie 1
        rs{length(rs)+1} = stB; % adds position to restricted
    end
end
%----------------------------------------------------------------------
output = [visitedF,visitedB];
fprintf('Failure\n')
end