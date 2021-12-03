n = 10
a = [['.']*n for i in range(n)]


"""
i = 0
j = (n-1)//2
a[i][j] = 1

# odd magic square
for k in range(2, n*n+1):
    if (k-1)%n==0:
        i += 1
    elif i==0:
        i = n-1
        j += 1
    elif j==n-1:
        i -= 1
        j = 0
    else:
        i -= 1
        j += 1

    a[i][j] = k
"""

# 10x10 matrix with dots.. ?
# want to replace 5 chars to @
# matrix manipulation
for i in range(5):
    for j in range(i*2+1):
        a[i+1][5-i+j] = '@'


# display matrix
for i in a:
    for j in i:
        print(f'{j:2}', end='')
    print()