import sys
N = int(sys.stdin.readline())
ck = [0] * N
for now in range(N):
    card = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in range(3):
        for j in range(i+1, 4):
            for k in range(j+1, 5):
                cnt = card[i] + card[j] + card[k]
                if ans < cnt%10:
                    ans = cnt%10
    ck[now] = ans
for i in range(N):
    if ck[i] == max(ck):
        ans = i+1
print(ans)