# 완전 방향을 잘못잡았다
import sys
K, N = map(int, sys.stdin.readline().split())
lanson = []
for _ in range(K):
    lanson.append(int(sys.stdin.readline()))

start = 0
end = max(lanson)
answer = 0

while start <= end:
    mid = (start+end)//2
    num = 0    # 랜선의 길이를 mid로 나누었을때 생성되는 랜선의 개수
    for lan in lanson:
        num += lan//mid
    if num >= N:
        start = mid+1
        answer = max(answer, mid)
    else:
        end = mid-1

print(answer)