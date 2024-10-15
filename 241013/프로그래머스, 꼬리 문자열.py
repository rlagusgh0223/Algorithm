def solution(str_list, ex):
    answer = ''
    for strl in str_list:
        if ex not in strl:
            answer += strl
    return answer

import sys

st = list(sys.stdin.readline().strip().split('", "'))
ex = sys.stdin.readline().strip()
print(solution(st, ex))