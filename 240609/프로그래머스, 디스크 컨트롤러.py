import heapq


def solution(jobs):
    # 총 소요 시간, 작업 시작 시간, 작업 종료 시간, 작업 수
    answer, start, end, cnt = 0, -1, 0, 0
    # 현재 시간 구간에서 작업 가능한 작업 저장할 리스트
    heap = []
    while cnt < len(jobs):
        # 작업 시작 시간이 이번 작업 구간 내에 있다면 리스트에 입력
        for s, e in jobs:
            if start < s <= end:
                heapq.heappush(heap, [e, s])
        # 지금 작업 가능한 시간이 있다면 그 중에서 작업시간 짧은것부터 작업한다
        if heap:
            job = heapq.heappop(heap)  # 작업 소요 시간이 가장 짧은 작업을 진행
            start = end  # 다음 시작 시간은 이번 작업 시간의 끝
            end += job[0]  # 현재 작업 소요 시간을 더해 작업 종료 시간 업데이트
            answer += end - job[1]  # 현재 작업의 시간을 더한다
            cnt += 1
        # 지금 작업 가능한 시간이 없으면 종료시간을 1 증가
        else:
            end += 1
    return answer // len(jobs)


import sys

jobs = list(sys.stdin.readline().strip().split("], ["))
jobs = [list(map(int, j.split(", "))) for j in jobs]
print(solution(jobs))