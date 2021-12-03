"""

1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42, …
분할수(number of partitions)는 자연수 n의 분할(partition)들 가운데, 원소가 중복되지 않는 것들의 개수입니다.
분할수는 p(n)으로 표기하는데 위의 숫자들은 p(0)=1 부터 시작한 분할수 수열입니다.
p(5)에 대한 예를 들겠습니다.

자연수 5의 분할은 다음과 같습니다.
1+1+1+1+1
2+1+1+1
2+2+1
3+1+1
3+2
4+1
5
개수가 7개입니다. 그러므로 p(5) = 7 입니다.

자연수 n을 입력 받아서,
p(n)을 구하여 보세요.

"""


def partition(n, k=1, s=''):
    if n==0:
        global total
        total += 1
        #print('+'.join(s))
    for i in range(k, n+1):
        partition(n-i, i, s+str(i))
        
def part_recursive(n, k):
    if n<0 or k==0: 
        return 0
    if n==0:
        return 1
    
    return part_recursive(n-k, k) + part_recursive(n, k-1)

#################################
n = int(input())
total = 0
# partition(n) 
print(total)

total =part_recursive(n, n)
print(total)