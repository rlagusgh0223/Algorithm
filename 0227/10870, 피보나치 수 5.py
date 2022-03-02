import sys
n = int(sys.stdin.readline())
f = [0, 1]    # 0번째 피보나치수는 0, 1번째 피보나치 수는 1

for i in range(2, n+1):
    f.append(f[i-1] + f[i-2])    # 2번째 피보나치 부터는 앞 두 피보나치 수의 합

print(f[n])