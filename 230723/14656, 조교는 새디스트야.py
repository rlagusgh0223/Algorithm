# 앞에사람의 번호와 비교하는게 아니라
# 1 2 3 4 5 이 순서에 맞지 않는 사람을 찾는거다import sys
import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
cnt = 0
for now in range(1, N+1):
    if now != lst[now-1]:
        cnt += 1
print(cnt)