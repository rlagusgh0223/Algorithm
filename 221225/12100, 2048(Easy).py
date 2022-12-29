def rotate90(B, N):
    NB = deepcopy(B)
    for i in range(N):
        for j in range(N):
            NB[j][N-1-i] = B[i][j]
    return NB

def convert(lst, N):
    new_list = [i for i in lst if i]
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0
    new_list = [i for i in new_list if i]
    return new_list+[0]*(N-len(new_list))

def dfs(N, B, count):
    ret = max([max(i) for i in B])
    if count == 0:
        return ret
    for i in range(4):
        X = [convert(i, N) for i in B]
        if X != B:
            ret = max(ret, dfs(N, X, count-1))
        B = rotate90(B, N)
    return ret

from copy import deepcopy
N = int(input())
Board = [list(map(int, input().split())) for _ in range(N)]
print(dfs(N, Board, 5))