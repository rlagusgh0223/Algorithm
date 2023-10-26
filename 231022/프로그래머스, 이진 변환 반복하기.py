# 모범답안
def solutions(s):
    cnt, zero = 0, 0  # 이진변환 횟수, 0 제거 길이
    while s != '1':
        cnt += 1
        num = s.count('1')
        zero += len(s) - num
        s = bin(num)[2:]  # bin() : 정수를 이진수로 만들어준다. 단, 맨앞에 0b가 붙는다
    return [cnt, zero]


# 내 풀이
def solution(s):
    answer = []
    cnt, zero = 0, 0  # 이진변환 횟수, 제거한 0의 개수
    while s != '1':
        ans = []  # 0 제거 후 문자열
        for i in s:
            if i == '0':
                zero += 1
            else:
                ans.append(1)
        now = len(ans)  # 0 제거 후 길이
        cnt += 1  # 0 제거했으므로 1 더한다
        # 길이를 이진 변환
        two = []
        while now > 1:
            two.append(now%2)
            now //= 2
        two.append(now)
        s = ''
        for t in range(len(two)-1, -1, -1):
            s += str(two[t])
    answer = [cnt, zero]
    return answer

import sys
s = sys.stdin.readline().rstrip()
print(solutions(s))