# 이전 풀이에선 answer[-1:] != [a]를 썼다
# answer[-1]!=a를 하면 answer가 비었을 경우에는 에러가 나오지만
# 둘 다 리스트인 answer[-1:]!=[a]를 하면 리스트가 비었더라도 
# 리스트 자체를 비교하는 것이므로 에러가 나오지 않는다

def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer

import sys

print(solution(list(map(int, sys.stdin.readline().split(",")))))
