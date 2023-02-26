# del을 쓰면 시간초과 난다
import sys
T = int(sys.stdin.readline())
for i in range(T):
    q = input()
    N, M = map(int, sys.stdin.readline().split())
    S = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    B = sorted(list(map(int, sys.stdin.readline().split())), reverse=True)
    while S and B:
        if S[-1] >= B[-1]:
            B.pop()
        else:
            S.pop()
    if S:
        print("S")
    elif B:
        print("B")
    else:
        print("C")