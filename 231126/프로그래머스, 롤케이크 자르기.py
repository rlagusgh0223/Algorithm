# Counter : 리스트의 값과 갯수를 딕셔너리로 만들어준다
from collections import Counter
def solution(topping):
    answer = 0
    # set으로 조사하면 시간초과 나온다
    # 우선 철수가 모든 롤케이크를 가지고 있다고 가정하고
    # 한 칸씩 잘라가며 비교해야 된다
    me = Counter(topping)
    bro = set()
    for t in topping:
        me[t] -= 1
        bro.add(t)
        # me[t]==0은 그 맛이 아예 없어진건데
        # 0으로 두면 len으로 계산이 되므로
        # 아예 딕셔너리에서 빼준다
        if me[t] == 0:
            me.pop(t)
        if len(me) == len(bro):
            answer += 1
    return answer

import sys
t = list(map(int, sys.stdin.readline().split(", ")))
print(solution(t))