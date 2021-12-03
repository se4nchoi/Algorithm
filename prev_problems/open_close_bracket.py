# n pairs of bracekts -- find number of possible valid comibnations

def valid_bracket(s, left, right, pair):
    if left == right == pair:
        # print(s)
        global count
        count += 1
    else:
        if left < pair:
            valid_bracket(s+'(', left+1, right, pair)
        if right < left:
            valid_bracket(s+')', left, right+1, pair)
            
# def par(n, s='', x=0):
#     global cnt
#     if n==0:
#         if x==0: cnt+=1
#         return
#     if x>=0:
#         par(n-1, s+'(', x+1)
#         par(n-1, s+')', x-1)

n = int(input())
count = 0
valid_bracket('', 0, 0, n)
print(count)

# cnt = 0
# par(n*2)
# print(cnt)

    

