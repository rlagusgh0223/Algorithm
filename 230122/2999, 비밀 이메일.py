import sys
m = sys.stdin.readline().rstrip()
N = len(m)
r, c, cnt = 0, 0, 0
for i in range(1, N//2+1):
    if N%i==0 and r<i and i<=N//i:
        r = i
        c = N//i
    # 주석 코드는 내 코드인데 위의 코드가 더 좋은것 같다
    # for j in range(N, i-1, -1):
    #     if j < i:
    #         break
    #     if i*j==N and i>r:
    #         r, c = i, j
lst = [['']*c for _ in range(r)]
for j in range(c):
    for i in range(r):
        lst[i][j] = m[cnt]
        cnt += 1
for now in lst:
    print(*now, sep='', end='')