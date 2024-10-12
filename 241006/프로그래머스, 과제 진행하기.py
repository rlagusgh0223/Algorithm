# 반례
# [["a","09:00","30"],["b","09:10","20"],["c","09:15","20"],["d","09:55","10"],["e","10:50","5"]]
# 기대값 : ["c","b","d","a","e"]
def solution(plans):
    answer = []
    
    # 시간 변환 (시간을 분 단위로 변환)
    for i in range(len(plans)):
        h, m = map(int, plans[i][1].split(":"))
        plans[i][1] = h * 60 + m  # 시작 시간을 분 단위로 변경
        plans[i][2] = int(plans[i][2])  # 소요 시간을 분으로 변환

    # 시작 시간 기준으로 정렬
    plans.sort(key=lambda x: x[1])

    stack = []

    # 과제들을 처리
    for i in range(len(plans)-1):
        # 다음 과제를 시작하는 시간
        time = plans[i+1][1]

        # 지금 과제를 다음 과제 전까지 마칠 수 있을 때
        if time >= plans[i][1] + plans[i][2]:
            time -= (plans[i][1] + plans[i][2])
            answer.append(plans[i][0])
            while stack and time>0:
                last = stack.pop()
                if last[1] <= time:
                    answer.append(last[0])
                    time -= last[1]
                else:
                    stack.append([last[0], last[1]-time])
                    break
        # 지금 과제를 다음 과제 전까지 마칠 수 없을 때
        else:
            last = [plans[i][0], (plans[i][1]+plans[i][2])-time]
            stack.append(last)

    answer.append(plans[-1][0])
    # 스택에 남은 작업 처리 (가장 최근에 멈춘 과제부터 처리)
    while stack:
        last = stack.pop()
        answer.append(last[0])
    
    return answer






import sys

plans = list(sys.stdin.readline().strip().split('"], ["'))
plans = [list(p.split('", "')) for p in plans]
print(solution(plans))