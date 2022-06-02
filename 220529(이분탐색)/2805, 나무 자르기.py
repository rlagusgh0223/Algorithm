# 13~15번째 줄은 시간초과 나온다
import sys
N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)

while start <= end:
    mid = (start+end)//2
    num = 0
    num = sum(i-mid if i-mid>0 else 0 for i in tree)
    # for i in tree:
        # if i >= mid:
        #     num += i-mid
    
    if num >= M:
        start = mid+1
    else:
        end = mid-1

print(end)