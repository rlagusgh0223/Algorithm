from collections import Counter


def solution(a):
    answer = 0  # 스타수열 길이
    star = Counter(a)  # 수열에서 나온 인자의 개수 저장할 리스트

    # a의 각 원소 s별로 스타 수열인지 확인
    for s in star.keys():
        # 현재 인자(s)의 개수가 스타 수열의 인자 횟수보다 작거나 같다면
        # 최대길이를 구하는 계산 의미 없다
        if star[s] <= answer:
            continue
        # 이번 인자로 스타 수열을 계산했을때 인자 횟수와 a의 인덱스
        cnt = idx = 0
        while idx < len(a) - 1:
            # 주어진 수열(a)의 이번(idx)과 다음 인덱스(idx)의 수가
            # 스타 수열의 조건에 만족하지 못한다면 다음 인덱스로 넘어간다
            if (a[idx]!=s and a[idx+1]!=s) or (a[idx]==a[idx+1]):
                idx += 1
                continue
            # 스타 수열의 조건에 만족한다면 인자 횟수 1 증가하고
            # 다음 인덱스도 세트이므로 다다음 인덱스로 넘어간다
            cnt += 1
            idx += 2
        answer = max(answer, cnt)  # 스타 수열 인자의 최대 횟수를 구한다
    return answer * 2  # 공통원소가 answer만큼 사용됐으면 실제 배열의 길이는 2배



import sys

a = list(map(int, sys.stdin.readline().split(",")))
print(solution(a))