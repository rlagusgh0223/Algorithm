# 음수 피보나치에서는 -짝수에서는 음수, -홀수에서는 양수다
# -7 ~ 7의 피보나치 수
# 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13
import sys
n = int(sys.stdin.readline())
f = [0, 1]
for i in range(2, abs(n)+1):
    f.append((f[i-1] + f[i-2]) % 1000000000)
if n<0 and abs(n)%2==0:
    print(-1)
elif n==0:
    print(0)
else:
    print(1)
print(f[abs(n)])