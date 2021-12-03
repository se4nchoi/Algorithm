"""
이진 검색(binary search)은 정렬된 배열에서 반씩 나누어 가며 item을 찾는 방법입니다. 검색 키를 전체의 가운데에서 찾고, 키가 작으면 왼쪽 반, 크면 오른쪽 반에서 찾습니다. 위의 그림은 7을 찾는 과정입니다.

키(key)와 오름차순으로 정렬된 배열을 입력 받아서,
recursive call 전략으로 키가 있는 배열의 index를 구하여 보세요.
없으면 -1을 출력합니다.
"""

def bin_search(arr, l, r, x):
    # make sure range is still relevant (i.e. not collapsed)
    if r > l:
        mid = (l + r-1) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return bin_search(arr, l, mid-1, x)
        else:
            return bin_search(arr, mid+1, r, x)

    else:        
        return -1

    


#################################################################
key = int(input())
array = list(map(int, input().split()))

n = bin_search(array, 0, len(array)-1, key)
print(n)