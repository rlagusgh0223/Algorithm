def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start = h1*60*60 + m1*60 + s1
    end = h2*60*60 + m2*60 + s2
    # 시작부터 정각인 경우는 계산에서 제외되므로 미리 더한다
    if start==0 or start==12*60*60:
        answer += 1
    while start < end:
        # 12시간(43200초)에 360도 = 120초에 1도 = 1초에 1/120도도
        nowh = (start/120) % 360
        # 60분(3600초)에 360도 = 10초에 1도 = 1초에 1/10도도
        nowm = (start/10) % 360
        # 60초에 360도 = 1초에 6도도
        nows = (start*6) % 360

        nxth = 360 if ((start+1)/120) % 360==0 else ((start+1)/120) % 360
        nxtm = 360 if ((start+1)/10) % 360==0 else ((start+1)/10) % 360
        nxts = 360 if ((start+1)*6) % 360==0 else ((start+1)*6) % 360

        if nows<nowh and nxts>=nxth:
            answer += 1
        if nows<nowm and nxts>=nxtm:
            answer += 1
        if nxth == nxtm == nxts:
            answer -= 1
        start += 1
    return answer

import sys

h1, m1, s1, h2, m2, s2 = map(int, sys.stdin.readline().split())
print(solution(h1, m1, s1, h2, m2, s2))