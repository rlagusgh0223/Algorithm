N = int(input())
B = list(map(int, input().split()))
for i in range(N):
    num = B[i]
    cnt = 0
    while num%3 == 0:
        num //= 3
        cnt += 1
    B[i] = (-cnt, B[i])
B.sort()
A = [x[1] for x in B]
print(*A, sep=' ')