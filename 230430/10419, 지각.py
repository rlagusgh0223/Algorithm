import sys
T = int(sys.stdin.readline())
for _ in range(T):
    d = int(sys.stdin.readline())
    s = 0
    while True:
        if (s+1)+(s+1)**2 <= d:
            s += 1
        else:
            break
    print(s)