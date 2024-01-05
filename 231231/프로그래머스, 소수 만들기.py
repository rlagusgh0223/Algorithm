import itertools
def solution(nums):
    answer = 0
    nums = list(itertools.combinations(nums, 3))
    for num in nums:
        now = sum(num)
        ck = True
        for i in range(2, int(now**0.5)+1):
            if now%i == 0:
                ck = False
                break
        if ck:
            answer += 1
    return answer


import sys
nums = list(map(int, sys.stdin.readline().split(",")))
print(solution(nums))