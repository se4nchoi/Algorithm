def dfs(i):
    path.append(i)

    for j in range(1, n+1):
        if j not in path and adj[i][j] == 1:
            dfs(j)

###########################################################
n = 6
adj = [[0 for k in range(n+1)] for x in range(n+1)]

links = [
    [1,2], [1,4], [1,5], 
    [2,4], 
    [4,3], [4,5], [4,6], 
    [5,3]
]

for l in links:
    i, j = l
    adj[i][j] = 1
    adj[j][i] = 1

print(adj)
###########################################################
s = 1
# can skip since visited dfs is only going for 1 traversal
# visited = [0] * (n+1) 
path = []

dfs(s)
print(path)


# if adj is given as input:
k = int(input())
a = ','.join(iter(input, ''))
b = a.split(',')
ad = [list(map(int, z.split())) for z in b] # list comprehension!
print(ad)