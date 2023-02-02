def check():
    k = int(sys.stdin.readline())
    lst = [sys.stdin.readline().rstrip() for _ in range(k)]
    for i in range(k):
        for j in range(k):
            if i == j:
                continue
            now = lst[i] + lst[j]
            ck = now[::-1]
            if now == ck:
                return now
    return 0

import sys
T = int(sys.stdin.readline())
for _ in range(T):
    print(check())