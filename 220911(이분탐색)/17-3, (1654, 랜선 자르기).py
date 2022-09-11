k, n = map(int, input().split())
lanson = []
for i in range(k):
    lanson.append(int(input()))
start, end = 0, 10000000000  # 0이 10개여야 맞는다. max(lanson)은 예전에는 맞은것 같은데 지금은 런타임 에러 뜬다
answer = 0
while start<=end:
    mid = (start+end) // 2
    num = 0
    for len in lanson:  # 랜선의 길이를 mid로 나누었을때 생성되는 랜선의 개수 num을 저장
        num += len//mid
    if num >= n:  # num이 n보다 크다면 start값 재지정
        start = mid + 1
        if mid > answer:  # num이 n보다 클대 answer값을 가장 큰 mid값으로 설정
            answer = mid
    else:
        end = mid - 1  # num이 n보다 작다면 end = mid-1
print(answer)