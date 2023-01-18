import sys
lst = [1]+[1] * (10**6)
ck = []
for i in range(2, len(lst)):
    if lst[i] == 1:
        ck.append(i)
        for j in range(2*i, len(lst), i):
            lst[j] = 0

N = int(sys.stdin.readline())
for _ in range(N):
    S = int(sys.stdin.readline())
    c = True
    for now in ck:
        if S%now == 0:
            print("NO")
            c = False
            break
    if c:
        print("YES")