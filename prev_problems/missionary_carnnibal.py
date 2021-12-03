
def get_boat_passengers(n):
    l = []
    # find all permutations
    for passengers in range(1,n+1):
        for missionary in range(passengers+1):
            cannibal = passengers-missionary

            # exclude when missionary is lower than cannibals
            # where missionary is on the boat
            if not (missionary!=0 and missionary < cannibal):
                l.append([missionary, cannibal])
                # l += [[missionary, cannibal]] # could also use this
    return l


def move(direction, state, solution, track=[]):
    print(state, '   ', track)
    if state==goal_state: 
        for a in solution:
            print(a)
        return

    s = list(state)

    for way in boat:
        m, c = way        

        # find numbers after move
        lm = s[0] - direction*m; lc = s[1] - direction*c; rm = s[2] + direction*m; rc = s[3] + direction*c
        k = [lm, lc, rm, rc,]

        condition1 = (lm >= 0 and lc >= 0 and rm >= 0 and rc >= 0)
        condition2 = (lm == 0 or lm >= lc) and (rm == 0 or rm >= rc)
        condition3 = (direction==1 and m+c >= 2) or (direction==-1)
        condition4 = [k]+[direction] not in solution
        
        # conditions look right after move, then traverse further
        if (condition1 and condition2 and condition3 and condition4):
            move(-direction, k, solution+[k]+[direction], track+[way])


# 3 missionary, 3 cannibals, 2 max passengers
m,c,p = 3,3,2
init_state = [m,c, 0,0]
goal_state = [0,0, m,c]
boat = get_boat_passengers(p)

sol = [init_state]

# direction 1 = left to right, -1 = right to left
move(1, init_state, [init_state]+1)

# lets see if we can apply moves and create the state space tree for the m&c problem

# we need to now differentiate left to right and right to left

# and then we need to check if the states make sense

# then see how we can achieve goal state
# --> with what ?? all the possibilities? or the best one