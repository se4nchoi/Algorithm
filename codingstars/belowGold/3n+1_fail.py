import time

inputs = []
for i in range(4):
    inputs.append(list(map(int, input().split())))

begin=time.time()

# process each line
# this is too brute force when n becomes large
# need to maybe do memoization:
# i.e. do not re compute the values we already have done
# save it... but there is also a memory problem but we will ignore

dict = {}
for k in range(len(inputs)):
    i = inputs[k][0]; ii = i
    j = inputs[k][1]; jj = j
    if i > j:
        i = jj
        j = ii
    interval = range(i, j+1)

    max_count = 0

    
    for n in interval:
        c = 0
        d = n
        if n in dict:
            c = dict[n]
        else:
            seq = []
            seq.append(n)
            while n > 1:
                if n % 2 == 0:
                    n = n // 2
                elif n % 2 == 1:
                    n = 3*n + 1
                seq.append(n)
            c = len(seq)
            dict[d] = c

        if c > max_count:
            max_count = c
                
    print(ii, jj, max_count)

end=time.time()
wall = end - begin
print(wall)



begin=time.time()
for i in range(100000):
    i = i
end=time.time()
print(end-begin)