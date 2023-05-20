import sys
n = int(sys.stdin.readline())
ans = 0
for i in range(1, n+1):
    if n%i == 0:
        ans += i
print((ans*5) - 24)