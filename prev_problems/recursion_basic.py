import string

# sum
def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)

# factorial
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

# change of base number
def jinbup(n, m, s=''):
    q = n // m
    r = n % m
    if q == 0:
        return jinbup_list[r] + s
    return jinbup(q, m, jinbup_list[r] + s)


input = list(map(int, input().split()))
jinbup_list = list(map(str, range(10)))+ list(string.ascii_uppercase+ string.ascii_lowercase)
print(jinbup(input[0], input[1]))
# print(fact(input))
# print(sum(input))
