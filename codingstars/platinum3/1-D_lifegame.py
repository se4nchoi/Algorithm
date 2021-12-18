"""
세포의 1차원 배열...
==========================
 0 | 1 | ...  | n-2 | n-1
==========================

세대에 걸쳐서 바뀌는 세포들.
다음세대를 형성하는 규칙은, i번째 세포가 i-1 i+1 세포를 보고, 두 이웃의 상태가 같으면
자신의 상태를 유지, 다르면 자신의 상태를 바꾼다.


같은 줄에 세포들의 현재 분포 상태와 n이 입력된다.
n은 제n세대를 의미한다.

Sample Input 1 

01100101 1
Sample Output 1

00011101
Sample Input 2 

10101000101111 5
Sample Output 2

10000110100011
"""
inputs = input().split()
cells = list(inputs[0])
n = int(inputs[1])

for gen in range(n):
    snapshot = cells.copy()
    for i, cell in enumerate(snapshot):
        # find neighbor
        left = snapshot[i-1]
        right = snapshot[(i+1)% len(snapshot)]
        if (left != right):
            if (cell == '0'):
                cells[i] = '1'
            else:
                cells[i] = '0'

print("".join(cells))