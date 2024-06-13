# permutation(순열) 이용하면 시간초과 나온다
def solution(numbers):
    # 모든 숫자를 문자로 바꾼다
    numbers = list(map(str, numbers))
    # 각 문자를 3번 반복한 값을 기준으로 내림차순 정렬한다
    # ex) 6 -> 666, 10 -> 101010, 2 -> 222
    # 이렇가 하면 1과 10이 있을때 1이 앞에 올 수 있다(110이 101보다 크다)
    numbers.sort(key=lambda x:x*3, reverse=True)
    # int로 한번 변환하여 혹시 앞에 있을 0을 제거한다
    # return할때 str(int)하는것 보다 이렇게 먼저 int로 바꾸고 하는게 더 빠르다
    answer = int(''.join(numbers))
    return str(answer)


import sys

numbers = list(map(int, sys.stdin.readline().split(", ")))
print(solution(numbers))


