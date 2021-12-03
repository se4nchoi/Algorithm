inputs = input().split()
cells = list(inputs[0])
n = int(inputs[1])

for gen in range(n):
    snapshot = cells.copy()
    for i, cell in enumerate(snapshot):
        # find neighbor
        left = snapshot[i-1]
        right = snapshot[(i+1)% len(snapshot)]
        if (left != right):
            if (cell == '0'):
                cells[i] = '1'
            else:
                cells[i] = '0'

print("".join(cells))