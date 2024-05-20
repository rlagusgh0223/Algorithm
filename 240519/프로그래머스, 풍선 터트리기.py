# 양 끝의 풍선의 값 보다 하나라도 작은 값의 풍선은 남을 수 있다
# 양 끝의 풍선은 반드시 남을 수 있다
def solution(a):
    # 풍선의 개수가 2개 이하라면 모든 풍선을 하나만 남길 수 있다
    if len(a) <= 2:
        return len(a)

    # 양 끝의 풍선은 반드시 남길 수 있으므로 2부터 시작한다
    answer = 2
    l, r = a[0], a[-1]
    for i in range(1, len(a)-1):
        if l > a[i]:
            l = a[i]
            answer += 1
        if r > a[-1-i]:
            r = a[-1-i]
            answer += 1
    # l과 r이 같다는 것은 하나의 풍선이 중복되서 계산됐다는 것이므로
    # 1을 빼고, 그렇지 않다는 것은 중복된 풍선이 없다는 것이므로 그대로 리턴한다
    if l == r:
        return answer - 1
    return answer


import sys

a = list(map(int, sys.stdin.readline().split(",")))
print(solution(a))