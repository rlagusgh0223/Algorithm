def go(n, x):
    if n == 0:
        if x == 0:
            return 0
        else:
            return 1
    elif x == 1:
        return 0
    elif x <= 1 + d[n-1]:
        return go(n-1, x-1)
    elif x == 1 + d[n-1] + 1:
        return p[n-1] + 1
    elif x <= 1 + d[n-1] + 1 + d[n-1]:
        return p[n-1] + 1 + go(n-1, x-1-d[n-1]-1)
    else:
        return p[n-1] + 1 + p[n-1]

n, x = map(int, input().split())
d = [0] * (n+1)
p = [0] * (n+1)
d[0] = 1
p[0] = 1
for i in range(1, n+1):
    d[i] = 1 + d[i-1] + 1 + d[i-1] + 1
    p[i] = p[i-1] + 1 + p[i-1]
print(go(n, x))