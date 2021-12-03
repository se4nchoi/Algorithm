"""
for int n = 5

1+1+1+1+1
1+1+1+2
1+1+3
1+2+2
1+4
2+3
5

자연수 분할(integer partition)은‘n이하의 정수들의 합이 n이 되는 수열’을 말합니다.
흔히 ‘덧셈 분해’라고 합니다.위의 예는 5의 분할입니다.순서가 바뀐 것은 중복이므로 의미가 없습니다.

정수 n을 입력 받아서,n을 분할하여 보세요.
"""

def partition(n, k=1, s=''):
    if n==0:
        print('+'.join(s))
    for i in range(k, n+1):
        partition(n-i, i, s+str(i))
        

#################################
n = int(input())
partition(n) 