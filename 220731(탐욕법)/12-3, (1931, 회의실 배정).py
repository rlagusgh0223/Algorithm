import sys
N = int(sys.stdin.readline())
meet = []
for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    meet.append([start, end])

meet.sort(key=lambda x:(x[1], x[0]))

answer = 0
endTime = 0

for i in range(N):
    if endTime <= meet[i][0]:
        endTime = meet[i][1]
        answer += 1

print(answer)