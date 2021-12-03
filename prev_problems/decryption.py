# Decryption technique
# 암호문 해독
from operator import xor


cyphertext = list(map(int, input().split()))
key = list(map(ord, list(input())))
result = ''

for i, c in enumerate(cyphertext):
    k = i % len(key)
    result += str(chr(xor(c, key[k])))

print(result)