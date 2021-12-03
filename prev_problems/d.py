def perm(r, s=''):
    # base case
    if (r==0):
        print(s)
        return
    
    for i in range(1,n+1):
        perm(r-1, s+str(i))



######

input = list(map(int, input().split()))
n = input[0]
r = input[1]

perm(r)