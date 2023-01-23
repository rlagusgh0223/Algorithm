import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
truck = [0] * 101
ans = 0
for i in range(3):
    x, y = map(int, input().split())
    for now in range(y, x, -1):
        truck[now] += 1
for i in range(101):
    if truck[i] == 3:
        ans += C * 3
    elif truck[i] == 2:
        ans += B * 2
    elif truck[i] == 1:
        ans += A
print(ans)