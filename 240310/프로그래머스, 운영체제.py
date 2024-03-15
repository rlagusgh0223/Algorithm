import heapq


# program[프로그램 점수, 호출된 시각, 실행 시간]
def solution(program):
    answer = [0] * 11
    n = len(program)
    program.sort(key=lambda x:x[1])
    idx = cur = 0  # 우선순위 정렬된 프로그램 중 실행 순서, 현재 시간
    wait = []  # heapq로 사용될 리스트

    # 현재 사용 가능한 시간인 프로그램들은 wait리스트에 heapq이용하여 입력
    def call():
        nonlocal idx
        while idx<n and program[idx][1]<=cur:
            heapq.heappush(wait, program[idx])
            idx += 1
    
    # 진행 가능한 프로그램이 있거나 대기중인 프로그램이 있을 경우
    while idx<n or wait:
        # 대기중인 프로그램이 하나도 없으면 다음 프로그램 받아온다
        if len(wait) == 0:
            cur = program[idx][1]
            call()
        now = heapq.heappop(wait)
        # 현재 프로그램에 대해 대기한 시간 입력하고
        answer[now[0]] += cur-now[1]
        # 현재 시간에는 현재 프로그램에 대한 종료시간을 더한다(프로그램 완료 시간)
        cur += now[2]
        call()

    answer[0] = cur
    return answer

import sys

program = list(sys.stdin.readline().strip().split("], ["))
program = [list(map(int, p.split(", "))) for p in program]
print(solution(program))