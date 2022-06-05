import sys
N = int(sys.stdin.readline())
check = [0]*10001
for i in range(N):
    x = int(sys.stdin.readline())
    check[x] += 1

for i in range(len(check)):
    if check[i] != 0:
        for j in range(check[i]):
            print(i)