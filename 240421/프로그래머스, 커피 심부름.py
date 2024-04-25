def solution(order):
    answer = 0
    for o in order:
        if o in ["iceamericano", "americanoice", "hotamericano", "americanohot",
                 "americano", "anything"]:
            answer += 4500
        elif o in ["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]:
            answer += 5000
    return answer

import sys

order = list(sys.stdin.readline().strip().split('", "'))
print(solution(order))
