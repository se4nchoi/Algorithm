# Q4 Hamiltonian Path
# node 15 is the target goal, where we need to start at node 0

# 
# 
#       IN COMPLETE!! 
# 
# 
# 
# 
# 
# 
# 
# 
# 


import networkx as nx
import numpy as np

# make 2d grid with nx
graph = nx.grid_2d_graph(4,4)

# make adjacency matrix
adj = np.array(nx.adjacency_matrix(graph).todense())

# use backtracking to check if our constraint can be met
# while finding the hamiltonian paths
path = []
v_start = 0
v_end = 15

hero = v_start

# hero needs to visit all nodes and close it
# if hero visits the room will close after he leaves 
# which he cannot enter again (edges are lost) 
# DFS, with backtracking

for curr_v in range(16):
    can_go = []
    for i, next_v in enumerate(adj[i]):
        if next_v == 1:
            can_go.append(i)

    if curr_v not in path:
        path.append(curr_v)
    
    # if curr_v == v_end and :
        


"""
a : 2d list (int)
room_number: int 
connected_rooms: list(int)

marks the room disconnected in the adj matrix
"""
def seal_room(a, room_number, connected_rooms):
    
    l = len(connected_rooms)
    for i in range(l):
        a[i][room_number] = 0