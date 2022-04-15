import sys
# 입력된 시간 리스트로 받는다
time1 = list(map(int, sys.stdin.readline().split(':')))
time2 = list(map(int, sys.stdin.readline().split(':')))

time2[0] += 24    # 시작시간에서 24시간 더하면 종료시간

# 시작시간에 종료를 하니 시작시간에서 현재시간을 빼면 남은 시간이 나온다
if time2[2] < time1[2]:    # 종료초가 현재초보다 초가 작을 경우 시간에서 60초를 가져온다
    time2[2] += 60
    time2[1] -= 1

if time2[1] < time1[1]:    # 종료 분이 현재 분보다 작을 경우 
    time2[1] += 60
    time2[0] -= 1

hour = time2[0] - time1[0]
minute = time2[1] - time1[1]
sec = time2[2] - time1[2]

# 임무를 시작한지 얼마 되지 않았을때 현재 시간이 시작 시간보다 숫자가 클 경우를 대비해 초반에 24를 더했다
# 그런데 시간이 꽤 지나 현재 시간이 시작 시간보다 숫자가 작을 경우 남은 시간은 24시간보다 커진다
# 이 경우를 대비하여 24를 다시 빼준다
if hour >= 24:
    hour -= 24

# 두 자리수가 아닐 경우 앞에 0을 붙여서 2자리로 만든다
if hour < 10:
    hour = '0' + str(hour)
if minute < 10:
    minute = '0' + str(minute)
if sec < 10:
    sec = '0' + str(sec)

print("{}:{}:{}".format(hour, minute, sec))