import sys
ans = int(sys.stdin.readline())
while True:
    now = sys.stdin.readline().rstrip()
    if now == '=':
        break
    res = int(sys.stdin.readline())
    if now == '+':
        ans += res
    elif now == '-':
        ans -= res
    elif now == '*':
        ans *= res
    elif now == '/':
        ans //= res
print(ans)