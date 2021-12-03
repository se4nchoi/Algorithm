"""
그래프의 모든 마디(node, 동그라미 부분)를 방문하는 방법들 중에서 너비 우선 검색(BFS:breadth-first search)은 빠르고 예외(error)가 없기 때문에 널리 사용된다.
BFS는 다음과 같이 진행된다.
‘출발점에서 시작하여 모든 이웃한 마디를 검색해 가는 방법이다. 즉, 가장 가까이 인접한 마디부터 차례로 모두 검색하고, 또 그곳으로부터 인접한 마디를 검색하는 것을 반복하여 끝까지 진행한다.’다음은 구체적인 방법이다.

①지정된 마디에서 출발한다.
②그 마디에 연결되어 있고, 방문하지 아니한, 번호가 작은 마디를 모두 방문한다.
③위에서 방문한 마디의 순서대로 ②의 과정을 반복한다.
④더 이상 방문할 마디가 없으면 끝낸다.

위의 graph에서 ①에서 출발한 경우는 다음과 같은 순서가 된다.
1 3 4 2 5 6 7
1에서 시작=>인접한 곳 3,4=>3의 인접한 곳 2=>2의 인접 7 등의 방법으로 진행된다.

임의의 마디에서 시작하여 BFS하라.

Sample Input
1
0 0 0 0 0 0 0 0
0 0 0 1 1 0 0 0
0 0 0 1 0 0 0 1
0 1 1 0 1 1 0 0
0 1 0 1 0 1 1 0
0 0 0 1 1 0 1 1
0 0 0 0 1 1 0 0
0 0 1 0 0 1 0 0

Sample Output 1
1 3 4 2 5 6 7 

"""
# que . pop(0) = get first 

def bfs(i):
    path.append(i)
    
    for j in range(1, n):
        if j not in path and adj[i][j]==1:
            que.append(j)
    while len(que) > 0:
        q = que.pop(0)
        if q not in path:
            bfs(q)



start = int(input())
a = ','.join(iter(input, ''))
b = a.split(',')
adj = [list(map(int, z.split())) for z in b] 

path = []
que = []
n = len(adj[0])

bfs(start)
print(' '.join(map(str,path)))