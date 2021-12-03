# Silver 3
a = int(input())
b = int(input())
c = int(input())

if (a > b):
    a += c
    b -= c
elif (a < b):
    b += c
    a -= c

print(a)
print(b)