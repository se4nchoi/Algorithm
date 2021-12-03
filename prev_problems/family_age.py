
max_age = 200
n = 0
kids = 9

# better way?
for youngest in range(1, max_age):
    for gap in range(1, max_age):
        oldest = youngest + gap*(kids-1)
        if oldest <= max_age:
            s = sum((x*x for x in range(youngest, oldest+1, gap)))
            # s = list(map(lambda x: x*x, range(youngest,oldest+1,gap)))
            parent_age = s**(0.5)            
            if parent_age <= max_age and parent_age==int(parent_age):
                print(f'{parent_age:10} {gap:10}')
                n+=1
print(n)
# for youngest in range(1, max_age):
#     kids_age = youngest

#     # sum up all other kids with same age gap
#     for gap in range(1,10):
#         # initialize sum with youngest child
#         s = youngest*youngest

#         # reset for each gap        
#         kids_age = youngest

#         # consider rest of chlidren
#         for j in range(kids-1):
#             kids_age += gap
            
#             if kids_age>max_age: break
#             s += kids_age*kids_age

#         # if the sum of children's age is an acutal sqaure, then we know that a parent age exists
#         r = s ** (0.5)
#         if r==int(r):
#             n+=1

# print(n)
