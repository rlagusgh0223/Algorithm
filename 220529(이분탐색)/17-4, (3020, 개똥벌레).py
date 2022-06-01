import sys

def lower(start, end, d, L):
    while start<=end:
        mid = (start+end)//2
        if L[mid] < d:
            start = mid+1
        else:
            end = mid
    return end

N, H = map(int, sys.stdin.readline().split())

up=[]
down=[]
result = []

for i in range(N):
    now = int(sys.stdin.readline())
    if i%2 == 0:
        up.append(now)
    else:
        down.append(now)

up.sort()
down.sort()

answer = 0
mx = 500001

for i in range(1, H+1):
    idxd = lower(0, len(down), i, down)
    idxu = lower(0, len(up), H-i+1, up)
    now = N//2-idxd + N//2-idxu
    result.append(now)
    mx = min(mx, now)

for ans in result:
    if ans == mx:
        answer += 1

print(mx, answer)