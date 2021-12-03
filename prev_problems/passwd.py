"""
중복되지 않은 문자 집합(character set)과 단어의 글자 수를 입력 받아서,
문자 집합의 문자로서 단어의 글자 수 이하의 패스워드(password)를 만들려고 합니다.
어떠한 패스워드를 만들 수 있을까요?
입력된 문자 집합의 순서대로 가능한 모든 패스워드를 출력하여 보세요.

    input
abc 2

    output
a
aa
ab
ac
b
ba
bb
bc
c
ca
cb
cc
"""
def word(n, set, s=''):
    if n==0:
        print(s)
        return
    if (s != ''):
        print(s)
    for char in set:
        word(n-1, set, s+char)

########################
input = list(input().split())
charset = input[0]
max = int(input[1])


word(max, charset)