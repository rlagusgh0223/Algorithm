def solution(n, lost, reserve):
    ck = [0] + [1]*n + [0]
    for l in lost:
        ck[l] -= 1
    for r in reserve:
        ck[r] += 1
    for i in range(1, n+1):
        if ck[i] == 0:
            if ck[i-1] > 1:
                ck[i-1], ck[i] = ck[i-1]-1, ck[i]+1
            elif ck[i+1] > 1:
                ck[i+1], ck[i] = ck[i+1]-1, ck[i]+1
    return len(ck) - ck.count(0)

import sys

n = int(sys.stdin.readline())
lost = map(int, sys.stdin.readline().split(", "))
reserve = map(int, sys.stdin.readline().split(", "))
print(solution(n, lost, reserve))