import sys
V = int(sys.stdin.readline())

# 띄어쓰기로 구분하지 않고 그냥 입력했으므로 rstrip()을 이용해서
# 마지막 '\n'만 안 받고 나머지는 하나씩 리스트로 넣는다
lst = list(sys.stdin.readline().rstrip())

Acnt = 0    # A와 B의 개수를 카운트할 변수
Bcnt = 0

# 입력한 문자 중 A와 B의 개수가 몇개인지 파악하는 반복문
for i in lst:
    if i == 'A':
        Acnt += 1
    else:
        Bcnt += 1

# 어느 문자가 더 많이 나왔는지 출력, 동일하다면 Tie 출력
if Acnt > Bcnt:
    print("A")
elif Acnt < Bcnt:
    print("B")
else:
    print("Tie")