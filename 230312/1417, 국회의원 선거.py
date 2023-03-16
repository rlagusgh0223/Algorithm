import sys
N = int(sys.stdin.readline())
lst = [0]*N
for i in range(N):
    lst[i] = int(sys.stdin.readline())
cnt = 0
while True:
    if lst[0]==max(lst) and lst.count(max(lst))==1:
        print(cnt)
        break
    now = lst.index(max(lst), 1)  # 1이 위치값을 말하는것 같다. 0, 1 순서로 lst[1] 부터 나오는 최대값
    lst[now] -= 1
    lst[0] += 1
    cnt += 1