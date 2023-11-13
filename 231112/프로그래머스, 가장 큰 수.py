def solution(numbers):
    answer =''
    numbers = list(map(str, numbers))
    # 문자열*3의 결과로 정렬하게 된다
    # [3, 30, 34, 5, 9]의 경우
    # [999, 555, 343434, 333, 303030]순으로 정렬된다
    numbers.sort(key=lambda x:x*3, reverse=True)
    answer = int(''.join(numbers))  # 000 같은 문자열이 나올 경우 0이 되게 한다
    return str(answer)

# permutations 이용한아래 코드는 시간 초과 나온다
# from itertools import permutations
# answer = sorted(list(map(''.join, permutations([str(n) for n in numbers]))))[-1]
import sys
numbers = list(map(int, sys.stdin.readline().split(", ")))
print(solution(numbers))