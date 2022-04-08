import sys
T = int(sys.stdin.readline())    # 테스트 케이스의 수 입력

for i in range(T):    # 테스트 케이스 수 만큼 반복
    school = []    # 테스트 케이스가 새로 시작될때마다 초기화
    drink = 0    # 술 소비량이 많은 학교를 확인하기 위한 변수 초기화
    cnt = 0    # 학교가 리스트로 입력되어 있으므로 출력때 사용할 변수
    N = int(sys.stdin.readline())    # 입력받을 학교의 수
    
    for j in range(N):
        x, y = sys.stdin.readline().split()    # x는 학교, y는 술 양인데 학교는 문자이므로 우선 그냥 띄어쓰기를 기준으로 문자로서 받는다
        y = int(y)
        school.append(list([x, y]))
        
        if drink < y:    # 이번에 술 마신 양이 이전까지 최고로 많이 마신양보다 많다면
            drink = y    # 마신 술(drinkg)과 리스트 위치(cnt) 변수 변경
            cnt = j

    print(school[cnt][0])