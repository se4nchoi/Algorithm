"""
두 정수 a, b의 최대공약수를 G(a, b)라고 하자.
정수 a, b, q, r (b ≠ 0)에 대하여 a = bq + r,이면 G(a, b) = G(b, r)가 성립한다.

최대공약수(GCD: Greatest Common divisor)
a를 b로 나눈 나머지를 r이라고 하자.
r이 0이면 gcd는 b이고, 아니면 a는 b, b는 r로 바꾸어 처음부터 반복한다.
최소공배수(LCM: Least common multiple)
lcm=a*b/gcd
"""


def euclidGCD(a, b):
    r = a % b
    if r == 0:
        return b

    return euclidGCD(b, r)

k = list(map(int, input().split()))
gcd = lcm = k[0]
for i in k[1:]:
    gcd = euclidGCD(gcd, i)
    lcm *= i // euclidGCD(lcm, i)

print(gcd, lcm)
