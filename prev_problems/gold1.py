# gold 1
a = int(input())

weight = (2,3,4,5,6,7,8,9,2,3,4,5)

for i in range(a):
    
    # #### USE MAP! #####
    id = input()
    s =  map(int, id[:6] + id[7:-1])
    k = 0
    last = int(id[-1])
    
    for w, n in enumerate(s):
        k += weight[w] * n
    v = (11 - (k % 11)) % 10    # the %10 takes care of 11 and 10
    print(v == last)
    
    
    
    
    
    
    
    
    # improvements: my original unpacking is REALLY not python-like.
    # use map() slicing to skip .split()
    # 
    
    """
    num = input()
    k = 0
    s = num.split("-")
    temp1 = s[0]
    temp2 = s[1]
    final = int(temp2[-1])       # last digit for verification
    
    
    # calculate weights
    w = 0
    for j in range(len(temp1)):
        k += weight[w] * int(temp1[j])
        w += 1        
    
    for j in range(len(temp2)-1):
        k += weight[w] * int(temp2[j])
        w += 1
    
    # verification
    v = k % 11
    if v == 10:
        v = 0
    if v == 11:
        v = 1
    else:
        v = 11 - v
        
    print(v == final)
    """