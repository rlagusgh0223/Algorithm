# pypy3로 해야 시간초과 안 난다
# n개의 점이 주어지면 각 점들마다 다른 점들과의 거리를 다 더한다(x,y)와 (y,x)는 다른 값이다
import sys
n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
ans = 0
for i in range(n):
    for j in range(n):
        ans += abs(x[i]-x[j])
print(ans)