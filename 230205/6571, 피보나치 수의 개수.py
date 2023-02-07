# 뭐때문인지는 모르겠는데 피보나치 수열을 0부터 만들어서 검증할때 0부터 시작하면 틀렸다고 나온다
# for now in f:    <- 이 부분...
# 피보나치 수열을 0부터 시작할거면 반복문을 1부터 시작해 검사하게 하면 되고
# 그냥 전부 다 검사하게 하려면 0에서 시작하지 않으면 된다
import sys
f = [1, 2]
now, i = 0, 2
while now <= 10**100:
    now = f[i-1] + f[i-2]
    f.append(now)
    i += 1
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a==0 and b==0:
        break
    cnt = 0
    for now in f:
        if a<=now<=b:
            cnt += 1
    print(cnt)