import sys
K, N = map(int, sys.stdin.readline().split())
lenson = []
for i in range(K):
    lenson.append(int(sys.stdin.readline()))
start = 1
end = max(lenson)
answer = 0
while start<=end:
    mid = (start+end) // 2
    num = 0
    for len in lenson:
        num += len//mid
    if num >= N:
        start = mid + 1
        if mid > answer:
            answer = mid
    else:
        end = mid - 1
print(answer)