import sys
K, N = map(int, sys.stdin.readline().split())
lanson = []
for i in range(K):
    lanson.append(int(sys.stdin.readline()))
start = 1
end = max(lanson)
answer = 0
while start<=end:
    mid = (start+end) // 2
    num = 0
    for lan in lanson:
        num += lan//mid
    if num >= N:
        start = mid + 1
        if answer < mid:
            answer = mid
    else:
        end = mid - 1
print(answer)