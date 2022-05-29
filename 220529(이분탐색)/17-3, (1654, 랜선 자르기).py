import sys
K, N = map(int, sys.stdin.readline().split())
lanson = []
for _ in range(K):
    lanson.append(int(sys.stdin.readline()))

start = 0
end = max(lanson)
answer = 0

while start <= end:
    mid = (start+end)//2    # 랜선의 길이가 가장 긴 값을 기준으로 중간값을 도출한다(랜선의 개수를 최소로 하기 위해?)
    num = 0    # 랜선의 길이를 mid로 나누었을 때 생성되는 랜선의 개수
    for lan in lanson:
        num += lan//mid    # 모든 랜선을 중간값으로 자른 몫을 더한다(랜선의 개수)
    if num >= N:    # 랜선의 개수가 목표값보다 많다면 더 길게 잘라야 하므로
        start = mid + 1    # start값 바꾼다
        answer = max(answer, mid)    # answer값을 가장 큰 mid값으로 설정(최대길이를 구해야 하므로)
    else:
        end = mid - 1

print(answer)