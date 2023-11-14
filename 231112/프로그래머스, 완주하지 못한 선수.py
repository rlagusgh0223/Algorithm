# 모범답안
# Counter : 동일한 객체가 몇개인지 딕셔너리 형태로 출력
from collections import Counter
def solution(participant, completion):
    # 딕셔너리끼리 빼진 못해도 Counter끼리는 뺄 수 있는것 같다
    # 딕셔너리로 직접 변환해서 빼보니까 에러 나옴
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
    # Counter 결과가 Counter({'mislav': 1})일때
    # answer.keys()로 나오는 출력 : dict_keys(['mislav'])
    # list(answer.keys())로 나오는 출력 : ['mislav']
    # 여기에서 list중 0번째 값을 출력하니 mislav만 나온다


# def solution(participant, completion):
#     answer = ''
#     part = dict()
#     for p in participant:
#         if p not in part:
#             part[p] = 1
#         else:
#             part[p] += 1
#     for c in completion:
#         part[c] -= 1
#     for key, value in part.items():
#         if value == 1:
#             answer = key
#     return answer


import sys
participant = list(sys.stdin.readline().strip().split('", "'))
completion = list(sys.stdin.readline().strip().split('", "'))
print(solution(participant, completion))