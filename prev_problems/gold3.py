# a = input()

# max = 0
# max_word = ''
# words = a.split()

# for word in words:
#     w = word.strip('.,!?')
#     l = len(w)
#     if l > max:
#         max = l
#         max_word = w
    
# print(l, max_word)
####################################################################
# a = input().split()
# week = [float(avg) for avg in a]

# ## or 
# week = map(float, input().split())
# count = 0
# for d in week:
#     if d <= 4.0:
#         count += 1

# print(count)
####################################################################

def recurse_n(n):
    if n < 1:
        return
    print(n, end=" ")
    recurse_n(n - 1)

n = int(input())
recurse_n(n)
