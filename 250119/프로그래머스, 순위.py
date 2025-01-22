def solution(n, results):
    check = [[0]*n for _ in range(n)]
    # 여기서 win-1, lose-1을 하지 않으면 밑의 계산에서 조금 더 길어진다다
    for win, lose in results:
        check[win-1][lose-1] = 1
        check[lose-1][win-1] = -1
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i==j or (check[i][j] in [1, -1]):
                    continue
                if check[i][k]==check[k][j]==1:
                    check[i][j]=1
                    check[k][i]=check[j][k]=check[j][i]=-1
    return sum(1 for ck in check if ck.count(0)==1)


import sys

n = int(sys.stdin.readline())
results = list(sys.stdin.readline().strip().split('], ['))
results = [list(map(int, r.split(", "))) for r in results]
print(solution(n, results))