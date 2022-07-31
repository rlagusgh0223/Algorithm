N = int(input())
A = list(map(int, input().split()))
S = int(input())

while True:
    tof = True
    for i in range(N):
        idx = i
        cmp = 0
        for j in range(N-1, i, -1):
            if A[idx]<A[j] and j-i<=S:
                idx = j
                cmp = j-i
                tof = False
        if idx != i:
            tmp = A[idx]
            del A[idx]
            A.insert(i, tmp)
            S -= cmp
    if tof:
        break

print(*A)