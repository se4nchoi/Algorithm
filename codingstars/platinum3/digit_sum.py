
def sum(n):
    if n == 0:
        return 0
    return n%10 + sum(n // 10)

cache = {0:0}
def sum_memo(n):
    if n not in cache:
        cache[n] = n%10 + sum_memo(n//10)
    return  cache[n]
##############
# do recursive method to find sum of the digits
num = int(input())

#print(sum(num))

# now use memoization
print(sum_memo(num))