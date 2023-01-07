import sys
N = int(sys.stdin.readline())
T = [(i*(i+1))//2 for i in range(45)]
ck = [0]*1001
for i in range(1, 45):
    for j in range(i, 45):
        for k in range(j, 45):
            now = T[i] + T[j] + T[k]
            if now <= 1000:
                ck[now] = 1
for i in range(N):
    K = int(sys.stdin.readline())
    print(ck[K])