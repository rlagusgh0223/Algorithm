def check(N, C):
    for i in range(N):
        if C[i]%2 == 1:
            C[i] += 1
    return len(set(C)) == 1

def teacher(N, C):
    tmp = [0 for _ in range(N)]
    for i in range(N):
        if C[i]%2 == 1:
            C[i] += 1
        C[i] //= 2
        tmp[(i+1)%N] = C[i]
    for i in range(N):
        C[i] += tmp[i]
    return C

def candy_war():
    N = int(input())
    C = list(map(int, input().split()))
    cnt = 0
    while not check(N, C):
        cnt += 1
        C = teacher(N, C)
    print(cnt)

T = int(input())
for _ in range(T):
    candy_war()