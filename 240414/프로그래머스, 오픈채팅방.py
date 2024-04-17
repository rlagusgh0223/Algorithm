from collections import defaultdict


def solution(record):
    answer = []
    dic = defaultdict(str)

    # Enter / Leave / Change 중 하나인데
    # Leave일 경우 닉네임을 생성하거나 바꾸는게 아니므로
    # Enter나 Change가 입력됐을때 딕셔너리의
    # 유저아이디 = 닉네임으로 바꾼다
    for r in record:
        r = r.split()
        if r[0] != 'Leave':
            dic[r[1]] = r[2]

    # Enter / Leave에 따라 다른 출력을 입력한다
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(dic[r[1]]))
        elif r[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(dic[r[1]]))
    return answer

import sys

record = list(sys.stdin.readline().strip().split('","'))
print(solution(record))