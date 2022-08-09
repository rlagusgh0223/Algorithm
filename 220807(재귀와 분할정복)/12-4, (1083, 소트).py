import sys
N = int(sys.stdin.readline())
A = [int(a) for a in sys.stdin.readline().split()]
S = int(sys.stdin.readline())

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
            S -= cmp
            A.insert(i, tmp)
    if tof:
        break

print(*A)