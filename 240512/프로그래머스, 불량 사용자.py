from itertools import permutations


# 해당 아이디 조합 중
# banned_id와 동일한 순서의 아이디가 제재 아이디와 같은지 확인
def check(user, banned_id):
    for i in range(len(user)):
        if len(user[i]) != len(banned_id[i]):
            return False
        for j in range(len(user[i])):
            if banned_id[i][j] == '*':
                continue
            if banned_id[i][j] != user[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    # 이번 문제는 banned_id의 순서와 수에 맞는 조합이 몇개인지를 찾는 문제이다
    # ex) 예제 1번 기준
    # banned_id = [fr*d*, abc1**]이면
    # [frodo, abc123] 와 [fradi, abc123] 이렇게 2가지 조합이 가능하므로
    # 2가 답이다
    # permutations를 이용해 banned_id의 수 만큼 조합 가능한 모든 경우의 수를 리스트한다
    user_list = list(permutations(user_id, len(banned_id)))
    answer = []  # 가능한 조합을 저장하기 위한 리스트
    # 조합들의 리스트에서 각 조합을 비교한다
    for user in user_list:
        if check(user, banned_id):
            # 중복을 막기 위해 집합 이용
            user = set(user)
            if user not in answer:
                answer.append(user)
    return len(answer)


import sys

user_id = list(sys.stdin.readline().strip().split('", "'))
banned_id = list(sys.stdin.readline().strip().split('", "'))
print(solution(user_id, banned_id))