

def bin(s):
    if (len(s)==n):
        print(s)
        return
    bin(s+'0')
    bin(s+'1')
    print(s)



n = 3
bin('')