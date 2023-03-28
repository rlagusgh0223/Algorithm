import sys
L = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline())
lst.sort()
cnt, start = 0, 1  # n < lst[0]일때 좋은구간은 1 ~ lst[0]-1이다. 초기값을 어떻게 주는지에 따라 반복문에서 start를 어떻게 할지 달라진다
if n in lst:
    print(cnt)
    exit()
for now in lst:
    if now < n:
        start = now+1
    else:  # n과 같은 경우는 위에서 이미 제외됐다
        end = now
        break
for i in range(start, end-1):
    for j in range(i+1, end):
        if i<=n<=j:
            cnt += 1
print(cnt)