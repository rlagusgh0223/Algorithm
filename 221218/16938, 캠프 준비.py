def go(index, cnt, tot, easy, hard):
    if index == N:
        if cnt>=2 and L<=tot<=R and hard-easy>=X:
            return 1
        else:
            return 0
    cnt1 = go(index+1, cnt+1, tot+A[index], min(easy, A[index]), max(hard, A[index]))
    cnt2 = go(index+1, cnt, tot, easy, hard)
    return cnt1+cnt2

N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))
print(go(0, 0, 0, 1000000, 0))