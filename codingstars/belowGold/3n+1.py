import time

inputs = []
for i in range(1):
    inputs.append(list(map(int, input().split())))


begin=time.time()

# process each input line
for k in range(len(inputs)):
    mn = inputs[k][0]
    mx = inputs[k][1]
    og_min = mn
    og_max = mx
    if mn > mx:
        mn, mx = mx, mn

    interval = range(mn, mx+1)
    
    # setting up the cache with base case
    cache = {1:1}
    
    # main loop to determine 3n+1
    max_count = 0
    for n in interval:
        num = n
        count = 0

        if n in cache:
            count = cache[n]
        else:
            # loop until we have a pre-calculated n 
            while n not in cache:
                if n % 2 == 0:
                    n = n // 2
                elif n % 2 == 1:
                    n = 3*n + 1
                count += 1
            # add to count from cache
            count += cache[n]       
                 
        # cache new-found n:count pair
        cache[num] = count

        # determine max count
        if count > max_count:
            max_count = count

    print(og_min, og_max, max_count)

end=time.time()
wall = end - begin
print(wall)