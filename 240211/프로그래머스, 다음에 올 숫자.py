def solution(common):
    # common의 길이는 3 이상이므로 0,1,2까지는 반드시 있다
    if common[2]-common[1] == common[1]-common[0]:
        return common[-1] + (common[2]-common[1])
    # 등차수열 아니면 등비수열이라고 했으므로 위의 경우의 수가 아니라면 등비수열이다
    return common[-1] * (common[2]//common[1])

import sys

c = list(map(int, sys.stdin.readline().split(", ")))
print(solution(c))