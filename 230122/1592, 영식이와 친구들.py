import sys
N, M, L = map(int, sys.stdin.readline().split())
ck = [0] * N
i = 0
while max(ck) < M:
    ck[i] += 1
    if ck[i]%2 == 1:
        i = (i+L)%N
    else:
        i = (i+(N-L))%N
print(sum(ck)-1)