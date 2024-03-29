N = int(input())    # 계수정렬로 입력
csortA = [0 for i in range(1002)]
csortB = [0 for i in range(1002)]

teamA = [int(x) for x in input().split()]
for i in range(N):
    csortA[teamA[i]] += 1
teamB = [int(x) for x in input().split()]
for i in range(N):
    csortB[teamB[i]] += 1

answer = 0

for i in range(1, 1001):    # 1~1000까지의 범위를 순회하며, 계수 i에 해당하는 csortA[i]가 (A팀) 존재한다면
    while csortA[i]:
        tof = False
        for j in range(i-1, 0, -1):    # i보다 작은 값 k가 B팀에 존재한다면 그 중 최댓값과 대결한다
            if csortB[j]:
                tof = True
                answer += 2
                csortA[i] -= 1
                csortB[j] -= 1
                break
        if tof == False:
            break

for i in range(1, 1001):    # 무승부가 가능한 경우를 구해준다
    while csortA[i] and csortB[i]:
        answer += 1
        csortA[i] -= 1
        csortB[i] -= 1

print(answer)