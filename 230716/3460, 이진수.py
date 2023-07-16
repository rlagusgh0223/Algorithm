import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    ans = []
    cnt = 0
    while n > 0:
        if n%2 == 1:
            ans.append(cnt)
        cnt += 1
        n //= 2
    print(*ans)