def solution(nums):
    return min(len(nums)//2, len(set(nums)))

import sys

nums = list(map(int, sys.stdin.readline().split(",")))
print(solution(nums))