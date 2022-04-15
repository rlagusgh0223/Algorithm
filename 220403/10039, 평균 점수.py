import sys
lst = []    # 5명의 점수를 받을 리스트
for i in range(5):    # 5명을 받는다고 정해졌으므로 5번 반복
    lst.append(int(sys.stdin.readline()))
    if lst[i] < 40:    # 40점 미만이면 보충수업을 받고 40점이 되며, 선택지가 없으므로 무조건 40점
        lst[i] = 40

print(sum(lst)//5)    # 각 점수의 합을 인원 수 로 나눠 평균으로 구하고, 정수가 나오게 한다