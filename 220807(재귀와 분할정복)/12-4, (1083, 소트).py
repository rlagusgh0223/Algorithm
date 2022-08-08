import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
s = int(sys.stdin.readline())

while True:
    tof = True
    for i in range(n):
        idx = i
        cmp = 0
        for j in range(n-1, i, -1):
            if a[idx]<a[j] and j-i<=s:
                idx = j
                cmp = j-i
                tof = False
        if idx != i:
            tmp = a[idx]
            del a[idx]
            a.insert(i, tmp)
            s -= cmp
    if tof:
        break

print(*a)