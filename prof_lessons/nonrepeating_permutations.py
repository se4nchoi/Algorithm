# non repeat!
# [1 2 3]
# 0 index switch with itself, i +1 ... i+ n-1
# and iterating for 1 index, 2 index

def perm(nums):
    track = []
    backtrack(nums, track)
    return res

    
def backtrack(n, t):
    # end condition: when permuted number t has max digit count
    if (len(t) == len(n)):
        res.append("".join(t))
        return
    
    for i in range(len(n)):
        if str(n[i]) not in t:
            t.append(str(n[i]))
            backtrack(n, t)
            t.pop()


def inplace(n, pivot=0):
    if(pivot > len(n)-1):
        return

    s = list(n)
    for i in range(len(n)):
        # make swap
        s[pivot], s[i] = s[i], s[pivot]
        st = ''.join([str(a) for a in s])
        if st not in res:
            res.append(st)
        inplace(s, pivot+1)
        s[i], s[pivot] = s[pivot], s[i]
    

# 기준점 매개체
# 간결한 교수님의 poem
# no need to check, no need to over iterate
def simple(index):
    if index == n:     
        print(''.join([str(a) for a in nums]))
        return
    
    for j in range(index, n):
        nums[index], nums[j] = nums[j], nums[index]
        simple(index+1)
        nums[index], nums[j] = nums[j], nums[index]     # reset before proceeding to next index


#################################################################
input = int(input())
nums = list(range(1, input+1))

n = input
simple(0)

res = []
# perm(nums)
# permmm = list(res)
# res = []
# inplace(nums)

# print(permmm)
# print(res)
# print(permmm.sort() == res.sort())

for line in res:
    print(line)