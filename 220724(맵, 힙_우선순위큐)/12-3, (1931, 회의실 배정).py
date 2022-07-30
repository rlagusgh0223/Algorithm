N = int(input())    # 회의실 상태를 입력받는다
meet = []

for i in range(N):
    A, B = map(int, input().split())
    meet.append([A, B])

meet.sort(key=lambda x:(x[1], x[0]))    # 회의가 끝나는 시간이 빠른 순으로, 끝나는 시간이 같다면 회의 시작 시간이 빠른 순으로 리스트를 졍렬한다

answer = 0    # 정답과 끝나는 시간을 저장하기 위한 변수를 생성한다.
endTime = 0

for i in range(len(meet)):
    if endTime <= meet[i][0]:    # 회의가 끝난 시간보다 시작 시간이 크다면 
        endTime = meet[i][1]    # 회의가 끝난 시간을 시작시간에 해당하는 회의가 끝난 시간 값으로 바꾸어 준다
        answer += 1    # 회의의 수 1 증가

print(answer)