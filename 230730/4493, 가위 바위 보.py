import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    p1, p2 = 0, 0
    for _ in range(n):
        x, y = sys.stdin.readline().split()
        if x == y:
            continue
        elif (x=='R' and y=='S') or (x=='S' and y=='P') or (x=='P' and y=='R'):
            p1 += 1
        else :
            p2 += 1
    if p1 > p2:
        print("Player 1")
    elif p1 < p2:
        print("Player 2")
    else:
        print("TIE")