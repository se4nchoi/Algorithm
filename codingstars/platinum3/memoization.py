
cache = {0:1}

def fact(n):
    if n not in cache:
        cache[n] = n * fact(n-1)
    return cache[n]

############
n = int(input())
print(fact(n))