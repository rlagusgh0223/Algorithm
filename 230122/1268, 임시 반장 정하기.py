import sys
input = sys.stdin.readline
N = int(input())
student = [list(map(int, input().split())) for _ in range(N)]
check = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(5):
        for k in range(N):
            if i==k or check[i][k]==1:
                continue
            if student[i][j] == student[k][j]:
                check[i][k] = 1
cap = [-1, 0]
for now in range(N):
    if cap[0] < sum(check[now]):
        cap[0], cap[1] = sum(check[now]), now+1
print(cap[1])