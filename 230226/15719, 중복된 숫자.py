# 문제가 파이썬에 맞지 않는것같다.
# split()으로 받으면 메모리 초과가 나므로
# 일단 문자열로 다 받은 다음 따로 계산을 해야된다
# 그러나 시간초과가 나므로 pypy3로 해야된다.
import sys
N = int(sys.stdin.readline())
A = sys.stdin.readline().rstrip()
temp = 0
cknum = ''
ck = sum(range(1, N))
for now in A:
    if now == ' ':
        temp += int(cknum)
        cknum = ''
    else:
        cknum = cknum + now
temp += int(cknum)
print(temp - ck)