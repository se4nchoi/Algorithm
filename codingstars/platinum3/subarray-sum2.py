"""
[1,2,3,4]의 부분 배열은 다음과 같이 16개가 있습니다.

[]
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 4]
[1, 3]
[1, 3, 4]
[1, 4]
[2]
[2, 3]
[2, 3, 4]
[2, 4]
[3]
[3, 4]
[4]
처음에 있는 blank list([])의 값을 0으로 계산하면
모든 부분 배열의 합(subarray sum)은 80입니다.

숫자로 된 배열을 입력 받아서,
부분 배열의 합을 구하여 보세요.


Input
숫자로 된 배열이 입력됩니다.
숫자는 정수입니다.


Output
부분 배열의 합을 출력합니다.

Sample Input 1 
3 26 -14 12 4 -2

Sample Output 1
928
"""

def subarraySum(i=0, s=[]):
    global total
    total += sum(s)
    if (i > n):
        return

    # duplicate check is here now (i, n); instead of checking duplicate, just skip the index
    for k in range(i, n):       
        subarraySum(k+1, s+[arr[k]])

######################
# sorting step makes it very hard when it comes to computation time.
# infact, it wasn't the sorting -- it was the range(n) --> range(i, n) that made a difference

# different approach:
# just sum it as you iterate

arr = list(map(int, input().split()))
n = len(arr)
total = 0
subarraySum()
print(total)