m = [
    'common',
    'leap'
]
y = 2024

# outside in
if y%4 ==0:
    if y%100 ==0:
        if y%400 ==0: 
            y=1 
        else: 
            y=0
    else: 
        y=1
else: 
    y=0

print(m[y])


# inside out
y=2024
if y%400==0:
    y=1
elif y%100==0:
    y=0
elif y%4==0:
    y=1
else:
    y=0
print(m[y])


# from the middle
y=2024
if y%100==0:
    if y%400==0:
        y=1
    else:
        y=0
elif y%4==0:
    y=1
else:
    y=0
print(m[y])

# logical aggregation
# put all the logical condition together
y = 2024
if (y%4 == 0 and y%100 != 0) or y%400==0:
    y = 1
else:
    y = 0
print(m[y])


########## CODING GOLF ?!
# one-liners
y = 2024
print(['common','leap'][y%4==0 and y%100!=0 or y%400==0])

