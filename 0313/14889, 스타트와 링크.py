# 오늘은 오후에 시험이 있어서 공부를 위해 프로그래밍 시간을 짧게 써야 하는데
# 시간이 다 되서 넘어간다
# 내일 코드 리뷰 후 주석 달겠다
import sys

def cal_diff(team1, team2):    # 팀의 능력치 차이를 계산하는 함수
    sum_team1 = 0
    sum_team2 = 0

    for i in range(len(team1)):
        for j in range(len(team1)):
            sum_team1 += arr[team1[i]][team1[j]]
            sum_team2 += arr[team2[i]][team2[j]]

    return abs(sum_team1 - sum_team2)

def make_team(team1, count, n, start):    # 팀을 구성하는 함수
    global answer

    if count == n//2:
        team2 = []
        for i in range(n):
            if i not in team1:
                team2.append(i)

        local_diff = cal_diff(team1, team2)
        answer = min(answer, local_diff)
        return

    for i in range(start, n):
        if i not in team1:
            team1.append(i)
            make_team(team1, count+1, n, i+1)
            team1.remove(i)

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = int(1e9)
make_team([], 0, n, 0)

print(answer)