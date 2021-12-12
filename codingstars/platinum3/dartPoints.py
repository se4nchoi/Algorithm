""" 
어떤 사람이 과녁에 화살 5번을 던졌는데 모두 과녁에 명중하였으며 점수의 합계가 100점이었습니다.
어디에 던졌을까요?
이러한 문제를 해결하여 봅시다.

화살을 던진 회수, 점수의 합계 그리고 과녁의 점수들을 입력 받아서,
어디에 던졌는가 구하여 보세요.


Input

첫째 줄에 화살을 던진 회수와 점수의 합계,
둘째 줄에 과녁의 점수들이 입력 됩니다.
모두 정수입니다.


Output

같은 줄에 화살이 꽂힌 과녁의 점수를 오름차순으로 출력합니다.
같은 점수가 여러 번이면 여러 번 출력합니다.


Sample Input 1 

5 100
5 9 27 36 48

Sample Output 1

5 5 27 27 36
"""

def getDartHits(i=0, s=[]):
    if (i == tries):   
        if(sum(s)==score):
            ss = sorted(s)
            if ss not in ans:
                ans.append(s)
        return

    # first print all possible scores
    for k in range(tries):
        getDartHits(i+1, s+[scoreBoard[k]])


inp = list(map(int, input().split()))
tries, score = inp[0], inp[1]
scoreBoard = list(map(int, input().split()))

ans = []
getDartHits()

for s in ans:
    print(' '.join(list(map(str, s))))
    