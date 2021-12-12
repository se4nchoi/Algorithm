"""
n_queens 문제는 n*n chessboard(체스 판)에 n개의 왕비가 서로 다투지 않도록 배치하는 모든 경우를 구하는 문제이다. 체스의 왕비는 가로, 세로, 대각선 방향으로 연속하여 이동할 수 있다. 그러므로 같은 행, 같은 열, 같은 대각선에 2개의 왕비가 있으면 안 된다.

아래의 그림은 8_queens 문제의 92가지 해결 방법 중의 하나이다.8개의 여왕은 서로 다투지 않는 위치에 있다.

. . . Q . . . .
. . . . . . Q .
. . Q . . . . .
. . . . . . . Q
. Q . . . . . .
. . . . Q . . .
Q . . . . . . .
. . . . . Q . .

n을 입력 받아서,
n*n 체스 보드에 n개의 왕비가 다투지 않도록 배치하는 방법의 수를 구하라.

HINT: 
 DFS, backtracking, tree-pruning;
 also, refer to diagonal with the following trick:
 i+j = constant == upper diagonal
 i-j = constant == lower diagonal
"""
