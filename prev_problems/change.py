"""

잔돈 지불 문제(counting change)는 금액을 동전 등으로 지불하는 방법을 구하는 문제입니다.

돈의 종류와 지불해야 하는 금액을 입력 받아서,
지불할 수 있는 방법의 수를 구하여 보세요.
돈의 종류마다 개수는 충분히 있습니다.

2 3 5 6 [available change order]
10      [total money]
--- >
5

(2 2 2 2 2)
5  5
3 5 2

"""

def giveChange(change, trail=''):
    if change == 0:
        m = trail.split()
        m.sort()
        if m not in ans:
            ans.append(m)
        return
    
    for bill in bills:
        if change >= bill:
            giveChange(change-bill, trail+str(bill)+' ')

###########
bills = list(map(int, input().split()))
total = int(input())
ans =[]
giveChange(total)
print(len(ans))