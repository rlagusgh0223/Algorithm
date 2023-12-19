def solution(numbers):
    answer = [i for i in range(10)]
    for n in numbers:
        answer[n] = 0
    return sum(answer)



import sys
numbers = list(map(int, sys.stdin.readline().split(",")))
print(solution(numbers))