import sys


# 부분합에서 최대값을 찾기 위해서는 부분합이 최소였던 지점부터 현재까지의 변화를 고려해야 합니다
# = 현재 누적합에서 이전 누적합의 최소값을 빼면 된다?
def solution(sequence):
    answer = -sys.maxsize
    sum1 = min1 = sum2 = min2 = 0
    p = 1
    for seq in sequence:
        # 누적합 구하기
        sum1 += seq * p
        sum2 += seq * -p

        # 최대 부분합 구하기
        answer = max(answer, sum1-min1, sum2-min2)

        # 누적합 중 최소값 구하기
        min1 = min(min1, sum1)
        min2 = min(min2, sum2)

        p *= -1
    return answer

sequence = list(map(int, sys.stdin.readline().split(", ")))
print(solution(sequence))