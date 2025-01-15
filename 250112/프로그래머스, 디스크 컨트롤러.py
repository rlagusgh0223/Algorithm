import heapq


def solution(jobs):
    answer, start, end, cnt = 0, -1, 0, 0
    heap = []
    while cnt < len(jobs):
        for begin, during in jobs:
            if start < begin <= end:
                heapq.heappush(heap, [during, begin])
        if heap:
            job = heapq.heappop(heap)  # 소요 시간이 가장 짧은 작업 꺼내기기
            start = end
            end += job[0]  # 이번 작업 소요 시간을 더한 작업 종료 시간
            answer += end - job[1]  # 작업 종료 시간 - 작업 시작 시간 즉, 이번 작업을 하기 위해 필요한 시간을 더한다
            cnt += 1  # 완료한 작업 수 증가
        else:
            # 이번 시간 구간 동안에 시작할 작업이 없다면 종료 시간 증가
            end += 1
    return answer // cnt

import sys

jobs = list(sys.stdin.readline().strip().split("], ["))
jobs = [list(map(int, j.split(", "))) for j in jobs]
print(solution(jobs))