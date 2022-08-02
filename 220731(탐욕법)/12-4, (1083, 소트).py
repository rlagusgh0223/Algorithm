import sys
N = int(sys.stdin.readline())
num = [int(x) for x in sys.stdin.readline().split()]
S = int(sys.stdin.readline())

while True:
    tof = True
    for i in range(N):
        idx = i
        cmp = 0
        for j in range(N-1, i, -1):
            if num[idx]<num[j] and j-i<=S:
                idx = j
                cmp = j-i
                tof = False
        if idx != i:
            tmp = num[idx]
            del num[idx]
            num.insert(i, tmp)
            S -= cmp

    if tof:
        break

print(*num)