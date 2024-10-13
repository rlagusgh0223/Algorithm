def solutions(n):
    answer = 0
    queen = [-1]*n

    def check(row, col):
        for i in range(row):
            if queen[i]==col or abs(queen[i]-col)==abs(i-row):
                return False
        return True

    def DFS(row):
        nonlocal answer
        if row == n:
            answer += 1
            return
        for col in range(n):
            if check(row, col):
                queen[row] = col
                DFS(row+1)
    DFS(0)
    return answer

# 더 좋아보이는 코드
answer = 0
ck = [False]*32
cross1 = [False]*32
cross2 = [False]*32
def check(x, n):
    global answer
    if x == n:
        answer += 1
        return
    for y in range(n):
        if not (ck[y] or cross1[x+y] or cross2[(y-x)+n]):
            ck[y] = cross1[x+y] = cross2[(y-x)+n] = True
            check(x+1, n)
            ck[y] = cross1[x+y] = cross2[(y-x)+n] = False

def solution(n):
    check(0, n)
    return answer

import sys

print(solution(int(sys.stdin.readline())))
