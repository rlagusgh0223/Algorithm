import sys
n = int(sys.stdin.readline())    # 테스트 케이스 수

for i in range(n):    # 테스트 케이스의 수만큼 반복
    Yonsei = [0]*9    # 연세대 점수를 입력할 리스트 초기화
    Korea = [0]*9    # 고려대 점수를 입력할 리스트 초기화
    for j in range(9):    # 매 경기는 9라운드니까 9번 반복
        x, y = map(int, sys.stdin.readline().split())    # 각 학교 점수 입력
        Yonsei[j] = x    # 매 경기(1회, 2회...9회) 점수를 각 학교 리스트에 입력
        Korea[j] = y

    # 연세대가 높은지 고려대가 높은지 점수가 같은지 출력
    if sum(Yonsei) > sum(Korea):
        print("Yonsei")
    elif sum(Yonsei) < sum(Korea):
        print("Korea")
    else:
        print("Draw")