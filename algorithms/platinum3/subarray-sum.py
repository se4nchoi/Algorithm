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

def subarraySum(i):
    pass

# use 2 indexes i, j to traverse each array's available subarray


######################
arr = list(map(int, input().split()))
array_set = {}
subarraySum()