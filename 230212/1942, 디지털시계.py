for _ in range(3):
    lst = list(input().split())
    H, M, S = map(int, lst[0].split(':'))
    h, m, s = map(int, lst[1].split(':'))
    cnt = 0
    while True:
        ans = H*10000 + M*100 + S
        if ans%3 == 0:
            cnt += 1
        if H==h and M==m and S==s:
            break
        S += 1
        if S == 60:
            S = 0
            M += 1
        if M == 60:
            M = 0
            H += 1
        if H == 24:
            H = 0
    print(cnt)