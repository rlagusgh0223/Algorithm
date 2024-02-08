# 모범답안
def solution(lines):
    # 파이썬 set에서 &는 교집합, |는 합집합이다
    sets = [set(range(l[0], l[1])) for l in lines]
    return len(sets[0]&sets[1] | sets[0]&sets[2] | sets[1]&sets[2])

def solutions(lines):
    answer = 0
    check = [0] * 200
    for line in lines:
        a, b = line[0]+100, line[1]+100
        for i in range(a, b):
            check[i] += 1
    for ck in check:
        if ck >= 2:
            answer += 1
    return answer


import sys
lines = list(sys.stdin.readline().strip().split("], ["))
lines = [list(map(int, lst.split(", "))) for lst in lines]
print(solution(lines))