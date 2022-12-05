def next_p(a):
    i = len(a) - 1
    while i>0 and a[i-1]>=a[i]:
        i -= 1
    if i <= 0:
        return False
    j = len(a) - 1
    while a[i-1] >= a[j]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def calc(a, b):
    n = len(a)
    ans = a[0]
    for i in range(1, n):
        if b[i-1] == 0:
            ans += a[i]
        elif b[i-1] == 1:
            ans -= a[i]
        elif b[i-1] == 2:
            ans *= a[i]
        else:
            ans = div(ans, a[i])
    return ans

def div(a, b):
    if a >= 0:
        return a//b
    else:
        return -(-a//b)

n = int(input())
a = list(map(int, input().split()))
cnts = list(map(int, input().split()))
b = []
for i, cnt in enumerate(cnts):
    for _ in range(cnt):
        b.append(i)
ans = []
while True:
    temp = calc(a, b)
    ans.append(temp)
    if not next_p(b):
        break
print(max(ans))
print(min(ans))