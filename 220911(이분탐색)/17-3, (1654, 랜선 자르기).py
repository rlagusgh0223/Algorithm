k, n = map(int, input().split())
lanson = []
for i in range(k):
    lanson.append(int(input()))
start = answer = 0
end = 10000000000
while start<=end:
    mid = (start+end)//2
    num = 0
    for lan in lanson:
        num += lan//mid
    if num >= n:
        start = mid + 1
        if mid > answer:
            answer = mid
    else:
        end = mid - 1
print(answer)