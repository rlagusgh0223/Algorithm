import sys
cnt = 0
n = list(sys.stdin.readline().rstrip())
while len(n) > 1:
    ans = 1
    for now in n:
        ans *= int(now)
    n = list(str(ans))
    cnt += 1
print(cnt)