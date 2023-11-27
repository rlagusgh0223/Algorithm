# product : 중복 순열
# permutation은 ('A', 'A')같은건 안되지만 product를 이용하면 나올 수 있다
from itertools import product
def solution(word):
    answer = []
    lst = ['A', 'E', 'I', 'O', 'U']
    # 알파벳은 1자리부터 5자리까지 가능하므로 가능한 문자열의 길이만큼 반복
    for i in range(1, 6):
        # 해당 문자열의 길이의 가능한 순열을 추출
        for l in product(lst, repeat=i):
            answer.append(''.join(l))
    answer.sort()
    return answer.index(word)+1


import sys
word = sys.stdin.readline().strip()
print(solution(word))