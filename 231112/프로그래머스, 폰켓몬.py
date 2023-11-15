def solution(nums):
    answer = min(len(nums)//2, len(set(nums)))
    return answer

import sys
nums = list(map(int, sys.stdin.readline().strip().split(",")))
print(solution(nums))