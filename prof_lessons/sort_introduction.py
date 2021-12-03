import copy
import time
import random


"""
does not return anything?!
"""
def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        flag = 0
        for j in range(n-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = 1

        # optimization: if the iteration is completed without
        # a swap ocrruing, then the array is in intended order
        if flag==0:break

        # this will reduce runtime by half on avg.

# selection sort

# this is basically finding the index of the smallest number
# and swapping current element of the array with the smallest number after finding the index
# this ensures that as i increases (the pointer moves further to the end of the array)
# the lowest indexes will be filled with the smallest number
def selection_sort(a):
    n = len(a)
    for i in range(n-1):
        # find the minimum index
        idx = i
        for j in range(i+1, n):
            if a[idx] > a[j]:
                idx = j
        a[i], a[idx] = a[idx], a[i]


# quicksort
def quick_sort(a):
    n = len(a)
    if n <= 1:
        return a
    pivot = a[n // 2]
    lesser, equal, greater = [], [], []
    for num in a:
        if num < pivot:
            lesser.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    return quick_sort(lesser) + equal + quick_sort(greater)

# TimSort


seed = random.seed(1)
k = 1000
a = []
for i in range(k):
    a.append(random.randint(1,10))

n = len(a)

a1 = copy.deepcopy(a)
a2 = copy.deepcopy(a)
a3 = copy.deepcopy(a)
a4 = copy.deepcopy(a)

print(f"for {k} size array")

# bubble sort
start = time.time()
bubble_sort(a1)
end = time.time()
t = end-start
print(f"bubble {0:4}: {t}s")

start = time.time()
selection_sort(a2)
end = time.time()
t = end-start
print(f"selection {0:1}: {t}s")

start = time.time()
a3 = sorted(a3)
end = time.time()
t = end-start
print(f"Timsort {0:3}: {t}s")

start = time.time()
a3 = sorted(a4)
end = time.time()
t = end-start
print(f"quicksort {0:1}: {t}s")

