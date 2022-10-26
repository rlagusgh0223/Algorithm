def check(a):
    n = len(a)
    ans = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if a[i][j] == a[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
        cnt = 1
        for j in range(1, n):
            if a[j][i] == a[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if ans < cnt:
                ans = cnt
    return ans

N = int(input())
a = [list(input()) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(N):
        if j+1 < N:
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
            temp = check(a)
            if ans < temp:
                ans = temp
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
        if i+1 < N:
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
            temp = check(a)
            if ans < temp:
                ans = temp
            a[i][j], a[i+1][j] = a[i+1][j], a[i][j]
print(ans)