# 문자열의 길이가 긴 놈의 원소가 아니라
# 문자열이 짧은것부터 시작해서 기존에 없던 값을 추가하여
# 최종적으로 가장 긴 문자열이 되면 그 리스트를 출력해야 된다
def solution(s):
    answer = []
    s = sorted(list(s[2:-2].split("},{")), key=len)
    for now in s:
        now = list(map(int, now.split(',')))
        for n in now:
            if n not in answer:
                answer.append(n)
    return answer


import sys
s = sys.stdin.readline().strip()
print(solution(s))