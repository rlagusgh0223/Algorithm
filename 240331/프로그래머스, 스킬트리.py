# 내 풀이와 같은 원리지만 파이썬의 문법을 더 다뤄서 남겨둔다
def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_sequence = list(skill)
        # for - else
        # for문이 break로 종료되지 않는다면
        # else 실행
        for sk in skill_tree:
            if sk in skill_sequence:
                # if문이 참이던 거짓이던 skill_sequence의 첫번째 값은 리스트에서 나온다
                if sk != skill_sequence.pop(0):
                    break
        else:
            answer += 1
    return answer

def solutions(skill, skill_trees):
    answer = 0
    for word in skill_trees:
        sk = list(skill)
        ck = True
        for w in word:
            if w in sk:
                if w != sk[0]:
                    ck = False
                    break
                else:
                    del sk[0]
        if ck:
            answer += 1
    return answer

import sys

skill = sys.stdin.readline().strip()
skill_trees = list(sys.stdin.readline().strip().split('", "'))
print(solution(skill, skill_trees))