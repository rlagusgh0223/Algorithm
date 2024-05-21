def solution(enroll, referral, seller, amount):
    answer = dict()  # 사람별 가진 돈을 저장할 딕셔너리
    human = dict()  # 사람별 소개해준 사람 저장할 딕셔너리
    for i in range(len(enroll)):
        human[enroll[i]] = referral[i]
        answer[enroll[i]] = 0

    # 민호 이외에 소개해준 사람이 있으며
    # 번 돈의 10%를 소개해준 사람에게 줄 수 있으면
    # 그 사람에게 10%의 돈을 주고 그 사람도 동일한 계산을 하는 DFS
    # 수수료 떼고 자기가 번 돈 추가한다
    def DFS(m, key, value):
        # m//10>0 부분 없으면 런타임 에러 나온다
        if value!='-' and m//10>0:
            DFS(m//10, value, human[value])
        answer[key] += m - m//10

    for i in range(len(amount)):
        m = amount[i] * 100
        DFS(m, seller[i], human[seller[i]])

    return list(answer.values())




import sys

enroll = list(sys.stdin.readline().strip().split('", "'))
referral = list(sys.stdin.readline().strip().split('", "'))
seller  = list(sys.stdin.readline().strip().split('", "'))
amount = list(map(int, sys.stdin.readline().strip().split(', ')))
print(solution(enroll, referral, seller, amount))