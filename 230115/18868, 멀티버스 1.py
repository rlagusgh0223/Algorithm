import sys
input = sys.stdin.readline
M, N = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(M)]
cnt = 0
for a in range(M-1):
    A = lst[a]
    for b in range(a+1, M):
        B = lst[b]
        for i in range(N):
            for j in range(i+1, N):
                if A[i]<A[j] and B[i]<B[j]:
                    ck = True
                elif A[i]==A[j] and B[i]==B[j]:
                    ck = True
                elif A[i]>A[j] and B[i]>B[j]:
                    ck = True
                else:
                    ck = False
                    break
            if not ck:
                break
        if ck:
            cnt += 1
print(cnt)