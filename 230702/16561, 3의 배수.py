import sys
n = int(sys.stdin.readline())
cnt = 0
# 반복문이 3개이면 시간초과가 나므로 반복문을 2개만 돌린다
for i in range(3, n, 3):
    for j in range(3, n, 3):
        k = n - i - j
        if k>0 and k%3==0:
            cnt += 1
print(cnt)