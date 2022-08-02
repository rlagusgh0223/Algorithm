import sys
N = int(sys.stdin.readline())
work = []
for i in range(N):
    work.append(list(map(int, sys.stdin.readline().split())))

work.sort(key=lambda x:(x[1], x[0]))

answer = 0
endTime = 0
for i in range(len(work)):
    if endTime <= work[i][0]:
        endTime  = work[i][1]
        answer += 1

print(answer)