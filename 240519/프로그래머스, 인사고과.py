# scores[0]에 있는 완호의 인센티브 등수가 몇인지 확인하는 문제
def solution(scores):
    answer = 1
    wa, wb = scores[0]

    # 근무 태도 점수는 내림차순, 동료 평가 점수는 오름차순
    scores.sort(key=lambda x:(-x[0], x[1]))
    # 첫번째 값을 내림차순, 두번째 값을 오름차순으로 했기 때문에
    # a값은 앞 순서의 값보다 작거나 같다
    # b값이라도 maxb보다 같거나 커야 두 점수 중 하나라도 같거나 큰 값이 나오므로
    # 인센티브 대상자가 된다 
    maxb = 0

    for a, b in scores:
        # 한번이라도 누군가의 두 점수보다 다 낮으면 인센티브 받지 못한다
        if wa<a and wb<b:
            return -1
        if maxb <= b:
            maxb = b
            # 지금 사람의 점수의 합이 완호보다 높으면 순위는 뒤로 밀려난다
            if a+b > wa+wb:
                answer += 1

    return answer


import sys

scores = list(sys.stdin.readline().strip().split("],["))
scores = [list(map(int, s.split(","))) for s in scores]
print(solution(scores))