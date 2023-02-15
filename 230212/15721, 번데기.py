import sys
A = int(sys.stdin.readline())
T = int(sys.stdin.readline())
n = int(sys.stdin.readline())
bundegi = []
bun = degi = 1
turn = 0
while True:
    pNum = bun
    turn += 1
    for _ in range(2):
        bundegi.append((bun, 0))
        bun += 1
        bundegi.append((degi, 1))
        degi += 1
    for _ in range(turn+1):
        bundegi.append((bun, 0))
        bun += 1
    for _ in range(turn+1):
        bundegi.append((degi, 1))
        degi += 1
    if pNum < T <= bun:
        print(bundegi.index((T, n))%A)
        break