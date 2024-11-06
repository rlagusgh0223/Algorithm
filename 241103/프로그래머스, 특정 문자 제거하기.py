def solution(my_string, letter):
    answer = ''
    for ms in my_string:
        if ms != letter:
            answer += ms
    return answer

    # 모범답안
    # return my_string.replace(letter, '')

import sys

ms = sys.stdin.readline().strip()
l = sys.stdin.readline().strip()
print(solution(ms, l))
