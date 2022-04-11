import sys
n = int(sys.stdin.readline())    # 테스트 케이스의 개수

for i in range(n):
    p = int(sys.stdin.readline())    # 고려해야될 선수의 수
    lst = []    # 선수 리스트. 테스트 케이스 마다 초기화
    money = 0    # 선수들의 연봉을 비교하기 위한 변수. 테스트 케이스마다 초기화
    for j in range(p):
        lst.append(list(sys.stdin.readline().split()))
        if money < int(lst[j][0]):
            money = int(lst[j][0])
            cnt = j    # 가장 연봉이 높은 선수의 순서를 저장하는 변수

    print(lst[cnt][1])