""" 
줄다리기(Tug of war)는 많은 사람이 두 편으로 나뉘어 줄을 마주 잡아당겨 승부를 겨루는 놀이입니다. 이와 같이 주어진 n 개의 정수 집합에 대해 n/2 크기의 두 가지 하위 집합으로 나눠서 두 집합의 합계의 차가 최소가 되도록 하여 봅시다. n이 짝수이면 두 개의 하위 집합의 크기는 엄격하게 n/2 이여야 하며, n이 홀수 인 경우 한 하위 집합의 크기는 (n-1)/2 이여야 하고 다른 하위 집합의 크기는 (n+1)/2 이여야 합니다.

예를 들어 주어진 집합을 {3, 4, 5, -3, 100, 1, 89, 54, 23, 20}으로 설정하면 집합의 크기는 10입니다.
이 집합의 출력은 {4, 100, 1, 23, 20} 및 {3, 5, -3, 89, 54}가 됩니다.
두 출력 부분 집합의 크기는 5이고, 두 부분 집합의 요소 합은 같습니다.(148 및 148).

n이 홀수 인 다른 예를 생각해 봅시다.
주어진 집합을 {23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4}이라고 합시다.
출력 하위 집합은 {45, -34, 12, 98, -1} 및 {23, 0, -99, 4, 189, 4}이 될 수 있습니다.
두 부분 집합의 요소 합계는 각각 120과 121입니다.

집합을 입력 받아서,
크기가 같고(홀수는 1개 차이), 요소(item) 합계 차이는 최소가 되도록 2개의 부분 집합으로 나누었을 때,
부분 집합의 요소 합계를 출력하여 봅시다.

*문제의 설명을 위하여 '집합' 이라는 용어를 사용하였지만 python으로 코딩할 때에는 집합 형(set type)의 사용을 피하여야 합니다. set type은 중복을 허용하지 않기 때문입니다.


// 결국은 하나의 배열이 주어졌을때 반으로 나뉘는 (or 1명의 차이) 최소한의 
// 차이로 나눠서 줄다리기를 하라는 소리...

Input

같은 줄에 집합의 요소들이 입력 됩니다.
모두 정수입니다.

Output

부분 집합의 요소 합계를 같은 줄에 작은 것부터 출력합니다.


Sample Input 1 
3 4 5 -3 100 1 89 54 23 20

Sample Output 1
148 148

Sample Input 2 
23 45 -34 12 0 98 -99 4 189 -1 4

Sample Output 2
120 121
"""
def getAllSubArray(i=0, s=[]):
    if (i == n//2):
        if sorted(s) not in subarr:
            subarr.append(s)
        return
    
    for k in range(i, n):
        if people[k] not in s:
            getAllSubArray(i+1, s+[people[k]])

def getOtherHalf(array):
    other = []
    for p in people:
        if p not in array:
            other.append(p)
    return other
    
################################################
people = sorted(list(map(int, input().split())))
subarr = []
n = len(people)
getAllSubArray()

m = people[-1]
min_diff_pair = 0
for s in subarr:
    other = getOtherHalf(s)
    pair = (s, other)
    diff = sum(s) - sum(other)
    if abs(0 - diff) < m:
        m = abs(0 - diff)
        min_diff_pair = pair
        
print(sum(min_diff_pair[0]), sum(min_diff_pair[1]))