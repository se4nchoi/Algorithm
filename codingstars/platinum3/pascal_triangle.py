import time

# n-th row's value is the sum of 2 numbers from n-1 th row's, excluding 1
def pascal(r):
    if r == 0:
        return

    # triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    pascal(r-1)

    row = [0 for x in range(r)]

    for c in range(r):
        # leftmost
        if c == 0:
            row[c] = 1
        else:
            # rightmost
            if c > r-2:
                row[c] = 1
            # other columns
            else:
                row[c] = triangle[r-2][c-1] + triangle[r-2][c]
            
    triangle.append(row)

def pascal_prof(n):
    if n not in cache:
        prev_row = pascal_prof(n-1)
        cache[n] = [ prev_row[i]+prev_row[i+1] for i in range(len(prev_row)-1) ]
        cache[n].insert(0, 1)
        cache[n].append(1)
    return cache[n]

triangle = []
n = int(input())

begin=time.time()
pascal(n+1)
print(' '.join(str(i) for i in triangle[n]))
end=time.time()
p = end-begin

begin=time.time()
cache = {0: [1]}
print(' '.join(str(j) for j in pascal_prof(n)))
end=time.time()
print("pascal: ", p)
print("pascal_prof: ", end-begin)

