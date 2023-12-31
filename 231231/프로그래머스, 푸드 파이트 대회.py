# 모범답안
def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i]//2)
    return answer + '0' + answer[::-1]


import sys
food = list(map(int, sys.stdin.readline().split(", ")))
print(solution(food))

def solutions(food):
    answer = ''
    ans = []
    for i in range(1, len(food)):
        if i%2 == 0:
            ans += list([i] * (food[i]//2))
        else:
            ans += list([i] * (food[i]//2))
    answer = ''.join(map(str,ans)) + '0' + ''.join(map(str,ans[::-1]))
    return answer