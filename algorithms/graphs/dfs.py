"""
위의 그래프의 ①에서 출발하면 1, 3, 2, 7, 5, 4, 6의 순서로 방문하게 된다.

그래프의 출발 위치와 인접 행렬(adjacency matrix)을 입력 받아서,
깊이 우선 탐색(DFS)한 탐색 순서를 출력하세요.


Input

첫째 줄에 탐색 시작 마디의 번호,
둘째 줄부터 그래프의 인접 행렬이 입력됩니다.
인접 행렬의 0번 행과 0번 열은 0이고, 끝에는 ''(null)이 있습니다.

"""

def dfs(i):
    path.append(i)

    for j in range(1, n):
        if j not in path and adj[i][j] == 1:
            dfs(j)


start = int(input())
a = ','.join(iter(input, ''))
b = a.split(',')
adj = [list(map(int, z.split())) for z in b] 

path = []
n = len(adj[0])

dfs(start)
print(' '.join(map(str,path)))