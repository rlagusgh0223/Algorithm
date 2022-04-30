# 식 = (의상 종류 1에서 선택 가능한 수 + 1)*(의상 종류 2에서 선택 가능한 수 + 1)*...
# ...*(의상 종류 n 에서 선택 가능한 수 + 1)-1(옷을 입지 않은 경우)
import sys
T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    cnt = 1    # 며칠동안 가능한지 나타낼 변수
    clothes = {}    # 의상의 종류를 입력할 딕셔너리
    for j in range(N):
        name, kind = sys.stdin.readline().split()
        if kind in clothes:    # 이미 있는 종류의 의상이라면
            clothes[kind] += 1    # 종류에 하나 추가
        else:    # 없는 종류의 의상이라면
            clothes[kind] = 1    # 1부터 시작(의상의 이름까지는 알 필요 없다)
    for kind in clothes:    # clothes의 키값(옷 종류)을 kind에 입력
        cnt *= (clothes[kind]+1)    # clothes의 values+1을 계속 곱한다
    print(cnt-1)    # 식에 맞춰 마지막에 1 빼준다(벌거벗을 경우)