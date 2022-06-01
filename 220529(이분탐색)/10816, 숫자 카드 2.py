# 시간초과 - 미리 숫자를 카운트 하고 출력
import sys
N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
lst.sort()

cnt = {}
for i in lst:
    if i not in cnt:
        cnt[i] = 1
    else:
        cnt[i] += 1

def check(now):
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if now == lst[mid]:
            break
        elif now < lst[mid]:
            end = mid-1
        else:
            start = mid+1
    if now == lst[mid]:
        return cnt[now]
    else:
        return 0
    

for i in range(M-1):
    print(check(arr[i]),end=' ')
print(check(arr[M-1]))