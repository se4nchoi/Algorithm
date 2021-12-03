

def get_mask(i):
    if i == 8:
        s,e,n,d,m,o,r,y = a[:8]
        send = 1000*s + 100*e + 10*n + d
        more = 1000*m + 100*o + 10*r + e
        money = 10000*m + 1000*o + 100*n + e*10 + y
        if (s != 0 and m != 0) and (send + more == money):
            print(send, more, money)
            print(s,e,n,d,m,o,r,y)

    for j in range(i, digit):
        a[i], a[j] = a[j], a[i]
        get_mask(i+1)
        a[i], a[j] = a[j], a[i]


def str_mask(i, x=''):
    if i == 8:
        s,e,n,d,m,o,r,y = x
        send = int(s+e+n+d)
        more = int(m+o+r+e)
        money = int(m+o+n+e+y)
        if (s != '0' and m != '0') and (send + more == money):
            print(send, more, money)
            print(x)


    for j in range(i, digit):
        a[i], a[j] = a[j], a[i]
        str_mask(i+1, x+a[i])
        a[i], a[j] = a[j], a[i]




def find_mask(i, x=''):
    # permutation complete
    if i == len(chars):
        # now assess if the assigned num-to-char is valid
        
        # apply permutation to the dictionary
        d = dict(zip(chars, x))
        # for k, v in enumerate(x):
        #     d[chars[k]] = v
        
        word1 = ''
        word2 = '' 
        word3 = ''
        for c in w1:
            word1 += d[c]
        for c in w2:
            word2 += d[c]
        for c in w3:
            word3 += d[c]
        
        # check if number is valid for each word (remove numbers with 0 start)
        # and satisfies the addition
        if ((word1[0] != '0' and word2[0] != '0' and word3[0] != '0') 
            and (int(word1) + int(word2) == int(word3))):
            print(word1, word2, word3)

    # find all permutations of number-to-character
    for j in range(i, digit):
        a[i], a[j] = a[j], a[i]
        find_mask(i+1, x+a[i])
        a[i], a[j] = a[j], a[i]
        
    

# digits
digit = 10
a = [str(i) for i in range(digit)]

d = {}
# assume all input will come in the following form in 1 line:
# word1 word2 word3
# and operation is always addition
# ie. word1 + word2 = word3

# w1, w2, w3 = input().split()
input = input().split()

# find unique characters of input
chars = []
w1 = input[0]
w2 = input[1]
w3 = input[2]
for w in input:
    for c in w:
        if c not in chars:
            chars.append(c)
print(chars)

# use set to extract unique characters
set_chars = list(set(w1+w2+w3))   
print(set_chars)
# drive code
find_mask(0)

# get_mask(0)
# str_mask(0)
