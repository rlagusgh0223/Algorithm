import sys
def lower(start, end, d, L):
    while start<end:
        mid = (start+end)//2
        if L[mid] < d:
            start = mid+1
        else:
            end = mid
    return end


N, H = map(int, sys.stdin.readline().split())
up = []
down = []
result = [0] * 500001
for i in range(N):
    x = int(sys.stdin.readline())
    if x%2==1:
        up.append(x)
    else:
        down.append(x)

up.sort()
down.sort()
answer = 0
mx = 1000000000000000

for i in range(1, H+1):
    idxd = lower(0, len(down), i, down)
    idxu = lower(0, len(up), H-i+1, up)
    result[i] = N//2-idxd + N//2-idxu
    mx = min(mx, result[i])

for i in range(1, H+1):
    if result[i] == mx:
        answer += 1

print(mx, answer)