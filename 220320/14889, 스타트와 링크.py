import sys

def cal_diff(team1, team2):    # 팀의 능력치 차이를 계산하는 함수
    sum_team1 = 0
    sum_team2 = 0

    for i in range(len(team1)):
        for j in range(len(team1)):
            print("cal_diff")
            print(team1)
            print(team2)
            sum_team1 += arr[team1[i]][team1[j]]    # 뭘 더하는건지?????????????????
            sum_team2 += arr[team2[i]][team2[j]]    # 정황상 ij나 ji로 구했을때 값을 각각 1, 2에 더하는것 같은데 뭔지 모르겠음

    return abs(sum_team1 - sum_team2)   # 팀의 차이값 리턴(ij와 ji)

def make_team(team1, count, n, start):    # 팀을 구성하는 함수
    global answer

    if count == n//2:   # count가 각 팀의 인원과 같다면
        team2 = []
        for i in range(n):
            if i not in team1:      # 어떻게 돌아가는건지?????????????????????????????????
                print('make_team')
                print(team1)
                print(i)
                print(i not in team1)
                team2.append(i)     # team2에 뭘 입력하는건지?????????????????????????????

        local_diff = cal_diff(team1, team2)     # cal_diff 함수에 team1과 team2값 입력
        answer = min(answer, local_diff)    # 최솟값 구하기
        return

    for i in range(start, n):   # 이번에 주어진 시작값부터 인원수까지
        if i not in team1:  # 재귀함수 사용
            team1.append(i)
            make_team(team1, count+1, n, i+1)
            team1.remove(i)

# 문제에서 주어진 입력
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

answer = int(1e9)   # answer는 최솟값을 구해야 되니까 지금은 가장 큰 값은 준다
make_team([], 0, n, 0)  # make_team 함수 호출(처음이니 초기값)

print(answer)