"""
알파벳과 숫자를 순서대로 짝을 지었습니다.
a=1, b=2, c=3, ..., z=26

입력된 숫자로 만들어 질 수 있는 모든 문자열을 찾아보세요.

다음은 예입니다.

입력:
1123

출력:
aabc ....... # a = 1, a = 1, b = 2, c = 3
aaw ........ # a= 1, a =1, w= 23
alc .......... # a = 1, l = 12, c = 3
kbc ......... # k는 11, b = 2, c= 3
kw .......... # k = 11, w = 23


Input

0이 포함되지 않은 숫자 열이 입력됩니다.


Sample Input 1 

21126

Sample Output 1

baabf
baaz
balf
bkbf
bkz
uabf
uaz
ulf
"""

# approach 1:
# get all permuatations of size 1-5 for every alphabet
# fail. for time efficiency
# def makeStrFromNum(cnt, s=''):
#     s_list = list(s)
#     ns = ''
#     for ch in s_list:
#         ns += str(d[ch])
#     if (ns == num):
#         print(s)
#         return
#     if (cnt==len(num)):
#         return
    
#     for i in range(0, len(abc)):
#         makeStrFromNum(cnt+1, s + abc[i])

# d = {}
# for i,v in enumerate(abc):
#     d[v] = i+1
# approach 2
# take the input number, divide it up then 
# stitch the split string with split or join
def makeStitchedNumber(cnt=0, s=''):
    if (cnt >= len(num)-1):
        s += num[cnt]
        stitched_num.append(s.split())
        return
    
    makeStitchedNumber(cnt+1, s + num[cnt]+ ' ')
    makeStitchedNumber(cnt+1, s + num[cnt]+ '')


num = input()
abc = [(chr(x)) for x in range(ord('a'), ord('z')+1)] # 'abcdefghijklmnopqrstuvwxyz'
stitched_num = []
d = {}
for i,v in enumerate(abc):
    d[str(i+1)] = v

makeStitchedNumber()

# now we have the stitched number
for k in stitched_num:
    include = True
    q = ''
    for n in k:
        if n in d:
            v = d[n]
            q += v
        else:
            include = False
            break
    if (include):
        print(q)


"""
This was about the approach to the problem.

Brute force was very exhaustive and slow.
If brute force is going to not cut it, need to 
1. optimize OR
2. change approach

Could not see optimization with approach 1.

In order to solve, we need to consider all cases -- but
need to make the consideration of all cases smaller.

We can disect the number itself, instead of generating the string
THEN matching it for the number.

QED
"""