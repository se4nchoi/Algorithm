"""
버전은 ‘1.1’, ‘1.0.23’, ‘2.10.5’ 등과 같이 점(‘.’)으로 구분된 문자열로서 표시한다.
2개의 버전을 비교하는 프로그램을 작성하라.
다음은 버전 비교의 예이다.

0.0.1 < 0.0.2
1.0.10 > 1.0.8
1.2 < 1.2.1
1.1 > 1.0.1
2.1.99 < 2.2.1
"""

# take a list of size 2 as p
# print comparison of the versions
# assumes each version is made up with 3 numbers 
# i.e.) a.b.c 
def compare(p):

    left = p[0].split('.')
    right = p[1].split('.')
    
    left_v = int(left[0])
    left_r = int(left[1])
    left_c = int(left[2])
    right_v = int(right[0])
    right_r = int(right[1])
    right_c = int(right[2])

    left = '.'.join(left)
    right = '.'.join(right)
    # compare version
    if left_v > right_v:
        print(left + ' > ' +right)
        return
    elif left_v < right_v:
        print(left + ' < ' +right)
        return
    # compare release
    elif left_r > right_r:
        print(left + ' > ' +right)
        return
    elif left_r < right_r:
        print(left + ' < ' +right)
        return
    # compare change
    elif left_c > right_c:
        print(left + ' > ' +right)
        return
    elif left_c < right_c:
        print(left + ' < ' +right)
        return
    else:
        print(left + ' = ' +right)
        return

inputs = [v.split() for v in input().split(',')]
for pair in inputs:
    compare(pair)