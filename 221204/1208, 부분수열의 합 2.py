n, s = map(int, input().split())
a = list(map(int, input().split()))
m = n//2
n -= m
first = [0] * (1<<n)
for i in range(1<<n):
    for k in range(n):
        if i&(1<<k) > 0:
            first[i] += a[k]
second = [0] * (1<<m)
for i in range(1<<m):
    for k in range(m):
        if i&(1<<k) > 0:
            second[i] += a[k+n]
first.sort()
second.sort(reverse=True)
n = 1<<n
m = 1<<m
i = j = ans = 0
while i<n and j<m:
    if first[i] + second[j] == s:
        c1 = c2 = 1
        i += 1
        j += 1
        while i<n and first[i] == first[i-1]:
            c1 += 1
            i += 1
        while j<m and second[j] == second[j-1]:
            c2 += 1
            j += 1
        ans += c1*c2
    elif first[i] + second[j] < s:
        i += 1
    else:
        j += 1
if s == 0:
    ans -= 1
print(ans)