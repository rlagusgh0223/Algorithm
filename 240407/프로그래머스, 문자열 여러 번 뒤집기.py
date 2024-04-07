def solution(my_string, queries):
    answer = list(my_string)
    for s, e in queries:
        answer[s:e+1] = reversed(answer[s:e+1])
        # reverse()는 부분 리스트가 역순으로 변경되지만,
        # 이 변경은 임시적인 리스트에 적용되고,
        # 실제로는 아무런 변화도 적용되지 않는다
        # 슬라이스에 대한 할당 연산에서는 reversed()가 적합하다
        # answer[s:e+1].reverse()
    return ''.join(answer)

import sys

my_string = sys.stdin.readline().strip()
queries = list(sys.stdin.readline().strip().split("], ["))
queries = [list(map(int, q.split(", "))) for q in queries]
print(solution(my_string, queries))