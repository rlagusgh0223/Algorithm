# 체스판을 가로(r), 세로(c)로 구분 했을 때
# 홀수일 때 가로를 자르고, 짝수일때 세로를 자르면 최대로 자른 값이 나온다
# 가로 / 세로로 자르는걸 번갈아서 하기만 한다면
# 짝수 / 홀수일때 자르는거 바뀌어도 상관없다
import sys
N = int(sys.stdin.readline())
r, c = 1, 1
for i in range(N):
    if i%2 == 0:
        r += 1
    else:
        c += 1
print(r*c)