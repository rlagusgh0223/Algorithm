import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    ans = n
    while n != 1:
        if n%2 == 0:
            n //= 2
        else:
            n = (n*3) + 1
        ans = max(ans, n)
    print(ans)