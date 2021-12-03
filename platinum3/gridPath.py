"""
격자의 행과 열의 크기를 입력 받아서,
격자의 왼쪽 위에서 오른쪽 아래로 가는 모든 최단 경로 (shortest grid path)를 d, r로 표시하여 보세요.

Input

같은 줄에 격자(grid)의 행(세로, row)과 열(가로, col)의 크기가 입력됩니다.

Output

격자의 왼쪽 위에서 오른쪽 아래로 가는 모든 최단 경로를 d, r로 표시하여 출력합니다.
출력 순서는 문제의 예와 같게 합니다.


Sample Input 1 

3 2

Sample Output 1

dddrr
ddrdr
ddrrd
drddr
drdrd
drrdd
rdddr
rddrd
rdrdd
rrddd
"""

def getGridPath(r, c, p=''):
    if (len(p) >= row+col):
        if (r==0 and c==0):
            print(p)
        return

    getGridPath(r-1, c, p+'d')
    getGridPath(r, c-1, p+'r')
    
a = input().split()
row, col = int(a[0]), int(a[1])

getGridPath(row, col)
