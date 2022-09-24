import sys

def lower(start, end, now, lst):
    while start<end:
        mid = (start+end)//2
        if lst[mid] < now:
            start = mid + 1
        else:
            end = mid
    return end

N, H = map(int, sys.stdin.readline().split())
up = []
down = []
for i in range(N):
    num = int(sys.stdin.readline())
    if i%2 == 1:
        up.append(num)
    else:
        down.append(num)
up.sort()
down.sort()
answer = 0
result = [0] * 500001
mx = 500000
for i in range(1, H+1):
    idxd = lower(0, len(down), i, down)
    idxu = lower(0, len(up), H-i+1, up)
    result[i] = N//2-idxd + N//2-idxu
    mx = min(mx, result[i])
for i in range(1, H+1):
    if result[i] == mx:
        answer += 1
print(mx, answer)