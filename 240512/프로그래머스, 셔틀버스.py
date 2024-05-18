def solution(n, t, m, timetable):
    # 크루가 역에 도착하는 시간 분으로 계산해서 오름차순 정렬한다
    # 그래야 버스 도착시간에 대입해서 계산할 수 있다
    timetable = [int(t[:2])*60+int(t[3:]) for t in timetable]
    timetable.sort()

    # 버스가 9시부터 n번 t분동안 판교역에 도착하는 시간
    busTime = [9*60+t*i for i in range(n)]

    i = 0  # 크루 인덱스
    # 버스에 탑승 가능한지 확인
    for bus in busTime:
        cnt = 0  # 버스에 탑승하는 승객 수
        # 버스에 탑승 가능한 자리가 있고 계산할 크루가 있으며
        # 그 크루가 버스에 탑승할 시간이 된다면(버스 도착 전이라면)
        while cnt<m and i<len(timetable) and timetable[i]<=bus:
            i += 1
            cnt += 1
        # 버스에 자리가 있으면 그 버스를 타면 된다
        if cnt < m:
            answer = bus
        # 자리가 없으면 탑승 가능한 크루 중 마지막 크루보다 1분 먼저 도착한다
        else:
            answer = timetable[i-1] - 1
    # zfill() : ()안의 숫자보다 문자열 자릿수가 부족하면 앞에 0을 채워 출력한다
    # 이미 ()안의 숫자보다 많으면 문자열을 그대로 출력한다
    return str(answer//60).zfill(2) + ':' + str(answer%60).zfill(2)

import sys

n, t, m = map(int, sys.stdin.readline().split())
timetable = list(sys.stdin.readline().strip().split('", "'))
print(solution(n, t, m, timetable))