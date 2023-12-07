# 걸리는 시간을 기준으로 이분탐색한다
# 즉, 처음 시작할때 left는 최소시간
# right는 가장 비효율적인 최대시간
# mid는 두 시간 사이
# people은 이 시간동안 검색하는 사람 수
def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    
    while left <= right:
        mid = (left+right) // 2
        people = 0
        # mid 시간 동안 심사관이 검사하는 사람 계산
        for time in times:
            people += mid//time
            # 시간이 남았어도 검사할 사람을 다 검사했으면 종료
            if people >= n:
                break
        # mid분 동안 심사한 인원에 따른 이분탐색
        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

import sys
n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
print(solution(n, times))