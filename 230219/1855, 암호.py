import sys
K = int(sys.stdin.readline())
lst = list(sys.stdin.readline().rstrip())
ans = [[0]*K for _ in range(len(lst)//K)]
for i in range(len(lst)//K):
    if i%2 == 0:
        for j in range(K):
            ans[i][j] = lst[i*K+j]
    else:
        for j in range(K):
            ans[i][j] = lst[i*K+(K-j-1)]
for i in range(K):
    for j in range(len(lst)//K):
        print(ans[j][i], end='')
print()