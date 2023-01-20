import sys
T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    room = [1] * (n+1)
    room[0] = 0
    for i in range(2, n+1):
        for j in range(i, n+1, i):
            room[j] = (room[j]+1) % 2
    print(sum(room))