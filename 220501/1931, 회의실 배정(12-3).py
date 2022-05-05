# 회의가 끝나는 시간이 작을수록
# 회의가 끝난 후 에는 시작 시간이 가까울수록
# 회의 시작 시간이 같다면 그 중 끝나는 시간이 작을수록
# 많은 회의를 할 수 있다
import sys
N = int(sys.stdin.readline())
conference = []
for i in range(N):
    conference.append(list(map(int, sys.stdin.readline().split())))

# x[1]회의가 끝나는 시간의 작은 값이 앞에오게 오름차순으로 정렬하되
# 끝나는 시간이 같다면
# x[0]회의가 시작하는 시간의 작은 값이 앞에오게 오름차순으로 정렬
conference.sort(key=lambda x: (x[1], x[0]))

answer = 0    # 회의의 수
endTime = 0    # 종료 시간

for i in range(N):    # 종료시간과 시작시간을 오름차순으로 비교한 모든 리스트 비교
    if endTime <= conference[i][0]:    # 회의가 끝난 시간이 다음 회의가 시작되는 시간보다 작다면
        endTime = conference[i][1]    # 그 회의를 수용하고 종료 시간에 그 회의의 종료시간을 입력한다
        answer += 1    # 회의를 한 것이므로 1 더해준다

print(answer)