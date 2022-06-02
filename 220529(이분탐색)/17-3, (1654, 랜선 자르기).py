# start와 end에 입력하는걸 잘못 생각했다
# answer에 mid를 넣어야 되는데 잘못 넣었다
# answer = max(answer, mid)를 쓰면 런타임 에러난다
import sys
K, N = map(int, sys.stdin.readline().split())
lanson = []
for _ in range(K):
    lanson.append(int(sys.stdin.readline()))

start = 1
end = max(lanson)
answer = 0

while start<=end:
    mid = (start+end)//2
    num = 0
    for lan in lanson:
        num += lan//mid
    if num >= N:
        start = mid+1
        if mid > answer:
            answer = mid
    else:
        end = mid-1
print(answer)