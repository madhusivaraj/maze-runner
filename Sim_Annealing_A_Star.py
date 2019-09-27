from MapCreator import *
from astar_manhattan import *
import random
import math
dim=100
p=.2
good_map=1
actualMap=[]
map_score=0
while good_map==1:
    actualMap=map_creator(10,0.2)
    map_score,xd=manhattan(actualMap)
    good_map=map_score

t=1
k=10
score_list=[map_score]
hardest_map=actualMap
hardest_map_score=map_score
i=0
for i in range(2000):
    new_map= actualMap
    dims=len(actualMap)-1
    good_map=1
    while good_map == 1:
        new_map[random.randint(0,dims)][random.randint(1,dims)]= random.randint(-1,0)
        new_map[0][0]=0
        new_map[dims][dims]=0
        new_map_score=(manhattan(new_map))[0]
        good_map=new_map_score
    if new_map_score> hardest_map_score:
        hardest_map=new_map
        hardest_map_score=new_map_score
    if new_map_score>map_score:
        actualMap=new_map
        map_score=new_map_score
    else:
        if random.random()<= math.exp(-k*(map_score-new_map_score)*t):
            actualMap= new_map
            map_score=new_map_score

    score_list.append(map_score)
    t+=1
print(score_list)
print(hardest_map_score)