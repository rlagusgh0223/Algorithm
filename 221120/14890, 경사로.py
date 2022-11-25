def go(a, l):
    n = len(a)
    c = [False] * n
    for i in range(1, n):
        if a[i-1] != a[i]:
            diff = abs(a[i-1] - a[i])
            if diff != 1:
                return False
            if a[i-1] < a[i]:
                for j in range(1, l+1):
                    if i-j < 0:
                        return False
                    if a[i-1] != a[i-j]:
                        return False
                    if c[i-j]:
                        return False
                    c[i-j] = True
            else:
                for j in range(l):
                    if i+j >= n:
                        return False
                    if a[i] != a[i+j]:
                        return False
                    if c[i+j]:
                        return False
                    c[i+j] = True
    return True

n, l = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    d = a[i]
    if go(d, l):
        ans += 1
for j in range(n):
    d = [a[i][j] for i in range(n)]
    if go(d, l):
        ans += 1
print(ans)