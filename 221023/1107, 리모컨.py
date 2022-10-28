import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken = [False] * 10
if M > 0:
    a = list(map(int, sys.stdin.readline().split()))
else:
    a = []
for i in a:
    broken[i] = True
def possible(c):
    if c == 0:
        if broken[0]:
            return 0
        else:
            return 1
    l = 0
    while c > 0:
        if broken[c%10]:
            return 0
        l += 1
        c //= 10
    return l
ans = abs(N-100)
for i in range(1000001):
    l = possible(i)
    if l > 0:
        press = abs(i-N)
        if ans > l + press:
            ans = l + press
print(ans)