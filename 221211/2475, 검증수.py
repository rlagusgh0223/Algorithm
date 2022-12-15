import sys
num = list(map(int, sys.stdin.readline().split()))
ans = 0
for now in num:
    ans += int(now) ** 2
print(ans%10)