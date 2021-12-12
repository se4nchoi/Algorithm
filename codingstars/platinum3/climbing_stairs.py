"""
5개의 계단을 한 번에 최대 3계단을 오를 수 있는 사람이 올라가는 방법은 13가지가 있습니다.

전체 계단의 수와 한 번에 최대 오를 수 있는 계단의 수를 입력 받아서,
올라갈 수 있는 모든 방법을 출력하여 보세요.

ex)
Input:
5 3

Output
1 1 1 1 1
1 1 1 2
1 1 2 1
1 1 3
1 2 1 1
1 2 2
1 3 1
2 1 1 1
2 1 2
2 2 1
2 3
3 1 1
3 2
"""

def climb(top, max_steps, ways=''):
    if (top == 0):              # reached top
        print(ways.strip())     # removes whitespace for format
        return
    for step in range(1, max_steps+1):
        # if taking the step will put you beyond the top of stairs, go back
        if (top - step < 0):
            return
        climb(top - step, max_steps, ways+str(step)+' ')
        # could also do " ".join(list) after putting the ways into a list

    

inputs = list(map(int, input().split()))
stairs = inputs[0]
max_step = inputs[1]

##
climb(stairs, max_step)

# improvements on speed = memoization to reduce computation