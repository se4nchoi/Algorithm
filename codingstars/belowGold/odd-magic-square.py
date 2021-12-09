"""
차수 n의 마방진은
정사각형에 1에서 n ^ 2까지의 정수를 가로, 세로, 대각선의 합이 같도록 배치한 것입니다.

가로, 세로, 대각선의 숫자 합을 마법 상수(magic constant)라 합니다.
마법 상수는 n으로 결정되는데 다음의 값을 가집니다.
M = n*(n ^ 2 + 1) / 2

n이 홀수인, 홀수 마방진은 드.라.루벨의 방법으로 만들 수 있습니다.

1은 첫째 줄 가운데 쓴다.
배수 다음은 아래에
첫째 줄 다음에는 오른쪽 가장 아래
가장 오른쪽 다음에는 위의 줄 첫 칸
그 외는 한 줄 위, 한 칸 오른쪽
홀수인 정수 n을 입력 받아서,
마법 상수를 구하고, 드.라.루벨의 방법으로 마방진을 만들어 봅시다.


Input

홀수인 정수 하나가 입력 됩니다.


Output

첫째 줄에 마법 상수를 출력하고,
다음 줄부터 마방진을 출력합니다.
마방진의 숫자 사이는 하나의 공백으로 분리합니다.


Sample Input 1 

5
Sample Output 1

65
17 24 1 8 15 
23 5 7 14 16 
4 6 13 20 22 
10 12 19 21 3 
11 18 25 2 9
"""
def increment(k):
    if (k+1 > n-1):
        return 0
    return k+1

def decrement(k):
    if (k-1 < 0):
        return n-1
    return k-1


n = int(input())
MC = n * (n*n + 1) // 2
print(MC)
ans = [[0 for x in range(n)] for x in range(n)]

# 1은 첫째 줄 가운데 쓴다.
# 행을 감소, 열을 증가 하면서 순차적으로 다음 숫자를 기입
# 행이 첫줄 보다 작아지면 마지막으로; 열이 마지막보다 커지면 첫열로
# 넣어야하는 숫자가 n의 배수면 행만 증가!
nums = list(range(1,n*n+1))
r, c = 0, n//2  # begin with 1

for num in nums:
    if num == 1:
        ans[r][c] = num
    else:
        # 숫자가 n의 배수 + 1
        if num%n == 1:
            r = increment(r)
        else:
            r = decrement(r)
            c = increment(c)

        ans[r][c] = num


# display answer
for r in ans:
    for num in r:
        print(num, end=' ')
    print()