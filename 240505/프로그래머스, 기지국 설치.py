def solution(n, stations, w):
    answer = 0
    std = 2*w + 1  # 한 기지국은 2*w + 1의 범위만큼을 담당할 수 있다
    start = 1  # 이전 영역과의 구분을 위한 변수
    
    # 모든 기지국을 기준으로 반복문
    for s in stations:
        # 지금 기지국으로부터 이전 기지국의 전파범위 밖의 범위
        # 또는 출발점까지의 범위 중 기지국을 설치해야 하는 경우
        if (s - w - start) > 0:
            # 현재 범위 내에서 2*w+1로 나눈 몫의 값이
            # 현재 범위에 설치해야 하는 기지국의 최소값이다
            answer += (s-w-start) // std
            # 만약 정확하게 나누어지지 않는다면
            if (s-w-start) % std:
                # 설치해야하는 기지국에 1을 추가한다
                answer += 1
        # 이번 기지국에서 담당 가능한 영역 다음의 영역을 start에 입력
        start = s + w + 1
    # 마지막 기지국보다 오른쪽에 있는 곳에 기지국의 설치가 필요할 경우
    if (n - start + 1) > 0:
        answer += (n-start+1) // std
        if (n-start+1) % std:
            answer += 1
    return answer

import sys

N = int(sys.stdin.readline())
stations = list(map(int, sys.stdin.readline().split(", ")))
W = int(sys.stdin.readline())
print(solution(N, stations, W))