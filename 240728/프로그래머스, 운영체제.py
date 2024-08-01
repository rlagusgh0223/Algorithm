import heapq


# 프로그램 점수, 호출시간, 실행시간
def solution(program):
    answer = [0] * 11  # 점수는 1점부터 10점까지 있지만, 총 11개의 값을 리턴하므로 11개의 리스트를 만든다
    n = len(program)
    idx = time = 0  # 현재 순서, 현재 시간
    wait = []  # 대기중인 프로그램을 저장할 리스트(우선순위 큐 사용)
    program.sort(key=lambda x:x[1])  # 호출시간 기준으로 정렬

    # 현재 시간 이전에 호출된 작업이 있다면 wait에 입력
    def call():
        nonlocal idx  # idx를 해당 함수에서 변경하므로 nonlocal 선언해줘야 한다
        while idx<n and program[idx][1]<=time:
            heapq.heappush(wait, program[idx])
            idx += 1

    # 실행할 작업이 남아있거나 대기중인 작업이 남아있다면 계속 실행
    while idx<n or wait:
        # 실행할 작업은 남아있지만 대기중인 작업이 없다면
        if not wait:
            time = program[idx][1]  # 다음 작업의 호출시간까지 기다린다
            call()  # 시간이 변경됐으므로 대기중인 작업이 있는지 확인한다

        now = heapq.heappop(wait)  # wait에서 우선순위가 가장 높은 작업을 가져온다
        answer[now[0]] += time - now[1]  # 해당 점수의 시간에 대기시간 누적(현재시간-호출시간)
        time += now[2]  # 현재시간에 작업시간 추가하여 다음 시간 구한다
        call()  # 시간이 변경됐으므로 대기중인 작업이 있는지 확인한다

    answer[0] = time  # 총 실행 시간을 answer[0]에 저장
    return answer

import sys

program = list(sys.stdin.readline().strip().split("], ["))
program = [list(map(int, p.split(", "))) for p in program]
print(solution(program))