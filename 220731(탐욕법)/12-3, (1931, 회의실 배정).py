import sys
N = int(sys.stdin.readline())
meeting = []
for i in range(N):
    meeting.append(list(map(int, sys.stdin.readline().split())))
meeting.sort(key=lambda x:(x[1], x[0]))

answer = 0
endTime = 0
for i in range(N):
    if endTime <= meeting[i][0]:
        endTime = meeting[i][1]
        answer += 1

print(answer)