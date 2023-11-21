import heapq
def solution(jobs):
    # 총 작업시간, 작업요청받는시작시간, 작업요청받는종료시간, 작업수행갯수
    answer, start, end, cnt = 0, -1, 0, 0
    heap = []
    # 모든 작업을 완료할 때까지 반복
    while cnt < len(jobs):
        for job in jobs:
            # 현재 작업의 요청시간이
            # 작업요청 받는 시작시간과 종료시간 사이에 있으면 heap에 넣는다
            if start < job[0] <= end:
                # 단, 작업소요시간을 기준으로 정렬하도록 소요시간과 요청시간의 위치를 바꿔준다
                heapq.heappush(heap, [job[1], job[0]])
        # 이번 시간 동안에 요청받은게 있다면
        if heap:
            # 그 중 가장 빨리 작업할 수 있는 작업을 시행한다
            job = heapq.heappop(heap)
            # 작업요청 받는 시작 시간은 지금 요청받는 종료시간으로 바꾸고
            start = end
            # 작업요청 받는 종료 시간은 지금종료시간+소요시간으로 한다
            # 어차피 해당 시간동안에는 작업 못하므로 그 시간동안에 요청있으면 접수받는다
            end += job[0]
            # 총 작업시간에는 지금 작업이 포함된 종료시간 - 요청시간을 더해준다
            answer += end - job[1]
            # 작업을 하나 완수했으므로 1 더해준다
            cnt += 1
        else:
            # 작업 가능한게 없다면 요청받는 작업 종료 시간을 1 더해준다
            end += 1
    return answer // len(jobs)


import sys
jobs = list(sys.stdin.readline().strip().split("], ["))
jobs = [list(map(int, job.split(", "))) for job in jobs]
print(solution(jobs))