"""
19880808
1988년 8월 8일은 서울 올림픽이 열린 날입니다.
19880808을 분할하여 사칙연산을 하여 100을 만드는 방법은 5가지가 있습니다.

1*9/8*80+80/8
1*98+80/8+0-8
1*98+80/8-0-8
1*98-8+0+80/8
1*98-8-0+80/8

숫자 열과 n을 입력 받아서,
숫자 열을 분할하여 사칙연산 한 결과가 n이 되는 모든 수식을 찾아보세요.

Sample Input 1 

7654321
100

Sample Output 1

7+6+54+32+1
7+65+4+3+21
7+65+4/3*21
7+65-4+32*1
7+65-4+32/1
7*6+5*4*3-2*1
7*6+5*4*3-2/1
7*6+54+3+2-1
76+5*4+3+2-1
76-5-4+32+1
76*5/4+3+2*1
76*5/4+3+2/1
76*5/4+3*2-1
"""
def makeN(counter, number, s=''):
    if (counter==len(number)-1):
        s += number[-1]
        try:        # just to avoid division by 0
            if eval(s) == n:
                print(s)
        except:
            pass    
        return      # end of recursion when counter at length of input number
    
    for op in ops:
        makeN(counter+1, number, s + number[counter] + op)
    
number = input()
n = int(input())
ops = ['+', '-', '*', '/', '']
makeN(0, number)

