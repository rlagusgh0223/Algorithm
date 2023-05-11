# pypy3로 제출해야 100점이 되고 python3로 내면 78점이 된다
# 아마 python3로는 문제를 푸는 시간이 부족한가 보다
import sys
N = int(sys.stdin.readline())
cnt = 0
for i in range(1, N+1):
    n = sum(map(int, str(i)))
    if i%n == 0:
        cnt += 1
print(cnt)