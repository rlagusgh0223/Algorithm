import sys
for _ in range(3):
    H, M, S, h, m, s = map(int, sys.stdin.readline().split())
    HMS = H*3600 + M*60 + S
    hms = h*3600 + m*60 + s
    hms -= HMS
    a = hms//3600
    b = (hms%3600) // 60
    c = (hms%3600) % 60
    print(a, b, c)