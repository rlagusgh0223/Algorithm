from collections import Counter

# Counter
# 객체를 세기 위한 딕셔너리 클래스
# ex)
# c = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
# print(c)  # Output: Counter({'b': 3, 'a': 2, 'c': 1})

def solution(clothes):
    answer = 1
    cloth = Counter([c[1] for c in clothes])
    # 해당 옷을 입지 않는 경우도 있을 수 있으므로
    # 옷의 종류에 1 더하고 계산한다
    for c in cloth.values():
        answer *= (c+1)
    return answer - 1  # 모든 옷을 입지 않는 경우는 제외한다

# # 경우의 수 계산식 : (종류 + 1) 곱하고 1 빼기
# ex. (a + 1)(b + 1)(c + 1) - 1
#  = (a + b + c) + (ab + bc + ca) + abc

import sys

clothes = list(sys.stdin.readline().strip().split('"], ["'))
clothes = [list(c.split('", "')) for c in clothes]
print(solution(clothes))