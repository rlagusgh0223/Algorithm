N, M = map(int, input().split())
a = [list(input()) for _ in range(N)]
check = [[False]*M for _ in range(N)]
ans = []
for i in range(N):
    for j in range(M):
        if a[i][j] == '*':
            l = 0
            k = 1
            while True:
                if i+k<N and i-k>=0 and j+k<M and j-k>=0:
                    if a[i+k][j]=='*' and a[i-k][j]=='*' and a[i][j+k]=='*' and a[i][j-k]=='*':
                        l = k
                    else:
                        break
                else:
                    break
                k += 1
            if l > 0:
                ans.append((i+1, j+1, l))
                check[i][j] = True
                for k in range(1, l+1):
                    check[i+k][j] = True
                    check[i-k][j] = True
                    check[i][j+k] = True
                    check[i][j-k] = True
for i in range(N):
    for j in range(M):
        if a[i][j]=='*' and check[i][j]==False:
            print(-1)
            exit()
print(len(ans))
for now in ans:
    print(' '.join(map(str, now)))