def go(index, first, second):
    if index == N:
        if len(first) != N//2:
            return -1
        if len(second) != N//2:
            return -1
        t1 = t2 = 0
        for i in range(N//2):
            for j in range(N//2):
                if i == j:
                    continue
                t1 += S[first[i]][first[j]]
                t2 += S[second[i]][second[j]]
        diff = abs(t1-t2)
        return diff
    if len(first) > N//2:
        return -1
    if len(second) > N//2:
        return -1
    ans = -1
    t1 = go(index+1, first+[index], second)
    if ans==-1 or (t1!=-1 and ans>t1):
        ans = t1
    t2 = go(index+1, first, second+[index])
    if ans==-1 or (t2!=-1 and ans>t2):
        ans = t2
    return ans

import sys
N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(go(0, [], []))