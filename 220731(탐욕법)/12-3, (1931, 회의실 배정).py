N = int(input())
meeting = []
for i in range(N):
    start, end = map(int, input().split())
    meeting.append([start, end])

meeting.sort(key=lambda x:(x[1], x[0]))

answer = 0
endTime = 0

for i in range(N):
    if endTime <= meeting[i][0]:
        endTime = meeting[i][1]
        answer += 1        

print(answer)