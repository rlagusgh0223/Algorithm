def check(row, col):
    if check_col[col]:
        return False
    if check_dig[row+col]:
        return False
    if check_dig2[row-col+N-1]:
        return False
    return True

def calc(row):
    if row == N:
        return 1
    ans = 0
    for col in range(N):
        if check(row, col):
            check_col[col] = True
            check_dig[row+col] = True
            check_dig2[row-col+N-1] = True
            a[row][col] = True
            ans += calc(row+1)
            check_col[col] = False
            check_dig[row+col] = False
            check_dig2[row-col+N-1] = False
            a[row][col] = False
    return ans

N = int(input())
a = [[False]*N for _ in range(N)]
check_col = [False] * N
check_dig = [False] * (2*N - 1)
check_dig2 = [False] * (2*N - 1)
print(calc(0))