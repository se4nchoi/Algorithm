"""
위의 그래프는 방향이 있고, cycle이 없으며, 반 순서 관계도 있다.
위상 정렬(topological sort)은 시작 위치에 따라 순서가 바뀔 수 있다.

위의 그래프를 1번 업무부터 연속적으로 파악하여 위상 정렬하라.

Sample Input 1 

0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0
0 1 0 0 0 1 0 0 0
0 0 0 0 1 0 0 1 0
0 0 0 0 0 0 0 0 0
0 0 0 0 1 0 1 0 0
0 0 0 0 0 0 0 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0

Sample Output 1

2 5 6 8 1 3 7 4 

#HINT:
위상정렬(topological sort)은 반 순서 관계가 있는 data에 대하여 제일 먼저
 하는 업무부터 마지막 업무까지 일렬로 나열하는 것이다.

‘반 순서 관계’에 대하여 설명한다.
위에 있는 그래프의 업무 계열은 (2,1,3,4,7), (2,5,4,6,7,8)의 
2개 계열이 있다. (업무 1)과 (업무 5)는 계열이 다르기 때문에 어느 업무를
 먼저 하여도 된다. 이와 같이 순서를 비교할 수 없는 경우가 있는 순서 관계를
 반 순서 관계(partial order)라고 한다.

업무 처리에 순서가 있고, 순서에 순환이 없는 업무 즉, 방향 있는 비 순환 
그래프(DAG: directed acyclic graph)는 위상 정렬을 할 수 있다. 
순환(cycle)이란, 위의 그래프에서 얘기하면, 7에서 3방향으로 연결되어 
있다면 (3,4,5,7)은 순환이 되어 업무 처리를 할 수 없다. 선행 작업을 
정할 수 없기 때문이다.‘닭이 먼저냐, 달걀이 먼저냐’이다. 순환이 있는 
그래프의 위상 정렬은 순환 위치를 표시하고 예외 처리를 하든가, 무시하고 
정렬할 수 있다. 위상 정렬은 작업 스케줄(job scheduling), mind map 작성,
 생물 계통 분류 등에 적용할 수 있다.

 should start at no incoming edge; (in-degree of 0)
"""

def topo(i):
    visited[i] = 1
    for j in range(1, n):
        if visited[j] != 1 and adj[i][j]:
            topo(j)
    
    stk.append(i)




a = ','.join(iter(input, ''))
b = a.split(',')
adj = [list(map(int, z.split())) for z in b] 

stk = []
visited = [0 for x in adj[0]]
n = len(adj[0])

topo(2) # start should be 2
print(' '.join(map(str,stk[::-1])))