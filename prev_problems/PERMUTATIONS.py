# PERMUTATIONS

# status space tree
# --> recursive call
# 전 영역 생성! 
# permutation

#               A 
#               /\
#             B    C
#             /\   /\
#            D  E  F G

# back-tracking, DFS
# promising ? --> pruning


# ?: get all possible (repeat-ok) 4digit number with 1,2,3

# function definition
def perm(n, s=''):
    # base case
    if (n==0):
        print(s)
        return
    
    for i in range(1,4):
        perm(n-1, s+str(i))
    # perm(n-1, s+'1')
    # perm(n-1, s+'2')
    # perm(n-1, s+'3')



##############      Application     ##############
def perm_string(n, s='', w=''):
    if n==0:
        print(s)
        return
    
    for char in w:
        perm_string(n-1, s+char, w)



def perm_op(n, ops, w, s=''):
    if n==0:
        print(s[:len(w)-1])
        return
    
    for num in w:
        s += num
        w = w[1:]
        for op in ops:
            perm_op(n-1, ops, w, s+op)
        

# 교수님 코드
# 연산자 문제
def perm_prof(n, s=''):
    # base case
    if (n==len(w)-1):
        s+=w[-1]
        try:
            print(eval(s))
            if eval(s) == 17:
                print(s)
        except:
            pass
        return
    
    for i in h_op:
        perm_prof(n+1, s+w[n]+i)

############### 100 만들기 문제 ###############
# +, -, ""(digit 합치기) ==> 100

def perm_hundred(n, number, ops, s=''):
    if (n==len(number)-1):
        s += number[-1]
        try:
            if eval(s) == 100:
                print(s)
        except:
            pass
        return
    
    for op in ops:
        perm_hundred(n+1, number, ops, s+number[n]+op)



# driver code
w = '050423'
ops = '+-*/'
op_list = list(ops).append('""')

a = '7654321'
ten = '123456789'
h_op = ['+', '-', '*', '/', '']
perm(4)     # 4 is the digit depth
perm_op(len(w), ops, w)
perm_prof(0)
perm_hundred(0, a, h_op, '')