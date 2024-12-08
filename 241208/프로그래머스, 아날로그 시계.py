def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start = h1*60*60 + m1*60 + s1
    end = h2*60*60 + m2*60 + s2
    # 시작부터 정각인 경우는 계산식에서 제외되므로 미리 계산한다
    # 현재 초침이 시침이나 분침보다 작지만,
    # 다음 초에 초침 위치가 시침이나 분침과 같거나 크다면 지나간걸로 간주
    if start == 0 or start == 12*60*60:
        answer += 1
    
    # start-1==end인 경우에 이미 end초까지의 경우의 수를 계산한다
    # 현재초에서 다음초 사이에 지나가는지를 보니까
    while start < end:
        # 현재 위치
        # 12시간 360도 = 1시간 30도 = 60분 30도 = 1분 1/2도 = 60초 1/2도 = 1초 1/120도
        nowh = (start/120) % 360  # 각도가 360도를 넘어가지 않도록 360으로 나눠준다
        # 60분 360도 = 1분 6도 = 60초 6도 = 1초 1/10도
        nowm = (start/10) % 360
        # 60초 360도 = 1초 6도
        nows = (start*6) % 360

        # 다음초 위치
        # 360도에 위치할경우 0으로 계산되므로0일땐 360으로 맞춰준다
        nxth = 360 if ((start+1)/120) % 360==0 else ((start+1)/120) % 360
        nxtm = 360 if ((start+1)/10) % 360==0 else ((start+1)/10) % 360
        nxts = 360 if ((start+1)*6) % 360==0 else ((start+1)*6) % 360

        # 현재초는 분침이나 시침보다 작지만
        # 다음초에 분침이나 시침과 같거나 커진다면 지나간걸로 계산
        if nows<nowh and nxts>=nxth:
            answer += 1
        if nows<nowm and nxts>=nxtm:
            answer += 1
        # 시침, 분침, 초침이 같을경우 중복으로 계산하므로 1 빼준다
        if nxth == nxtm == nxts:
            answer -= 1
        start += 1
    return answer

import sys

h1, m1, s1, h2, m2, s2 = map(int, sys.stdin.readline().split())
print(solution(h1, m1, s1, h2, m2, s2))