import sys
N, K = map(int, sys.stdin.readline().split())
cnt = 0
for i in range(N+1):
    ha = i//10
    hb = i%10
    for j in range(60):
        ma = j//10
        mb = j%10
        for k in range(60):
            ca = k//10
            cb = k%10
            if K in [ha, hb, ma, mb, ca, cb]:
                cnt += 1
print(cnt)