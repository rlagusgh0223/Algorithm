def solution(progresses, speeds):
    answer = []
    # progresses와 speeds를 각각의 인덱스별로 리스트로 만들고 p,s에 입력한다
    for p, s in zip(progresses, speeds):
        # 처음 값이거나 이전 값의 완료시간이 지금 완료일보다 적을경우
        # 올림효과를 내기 위해 음수연산을 해야한다
        if len(answer)==0 or answer[-1][0] < -((p-100)//s):
            # 남은 완료일과 1개의 기능을 새로 입력한다
            answer.append([-((p-100)//s), 1])
        # 이전 완료일에 맞춰 완료되므로 이전 완료일에 완성되는 기능을 1개 추가한다
        else:
            answer[-1][1] += 1
    # 각 완료일 별 기능 출력
    return [a[1] for a in answer]

import sys

progresses = list(map(int, sys.stdin.readline().split(", ")))
speeds = list(map(int, sys.stdin.readline().split(", ")))
print(solution(progresses, speeds))