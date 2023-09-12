# 버블정렬 문제
import sys
P = int(sys.stdin.readline())
for _ in range(P):
    ans = 0
    T = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(T)-1):
        for j in range(i+1, len(T)):
            if T[i] > T[j]:
                T[i], T[j] = T[j], T[i]
                ans += 1
    print(T[0], ans)