"""
1부터 9까지 연속된 숫자들을 순서를 바꾸지 않고 분할하여 사칙 연산을 하였을 때,
100이 되는 경우를 찾아보았습니다. 위와 같이 모두 101가지의 경우가 있었습니다.

양의 정수 n과 m을 입력 받아서,
1부터 n까지 숫자들을 순서를 바꾸지 않고 분할하여 사칙 연산을 하였을 때,
결과가 m이 되는 수식을 조사하여 보세요.

INPUT
5 30

OUTPUT
연산 결과가 m이 되는 수식을 문제와 같은 순서대로 한 줄에 하나씩 출력합니다.
찾는 수식이 없으면 출력하지 않습니다.(''(null)을 출력합니다)

1+2*3*4+5
1*2/3*45
1/2*3*4*5
"""

def perm_hundred(n, number, ops, s=''):
    if (n==len(number)-1):
        # append last digit
        s += number[-1]
        try:
            if eval(s) == target:
                print(s)
        except:
            pass
        return
    
    for op in ops:
        perm_hundred(n+1, number, ops, s+number[n]+op)


#################################
input = list(input().split())

nums = list(map(str, range(1,int(input[0])+1)))
target = int(input[1])
ops = ['+', '-', '*', '/', '']

perm_hundred(0, nums, ops)