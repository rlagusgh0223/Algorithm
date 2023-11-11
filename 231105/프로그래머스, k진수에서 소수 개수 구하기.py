def solution(n, k):
    answer = 0
    word = ''
    # k진수로 만들기
    while n:
        word = str(n%k) + word
        n //= k
    word = word.split('0')
    # 0을 기준으로 나눠진 k진수가 소수인지 판단
    for w in word:
        ck = True
        # w가 ''거나 2보다 작다면 비교대상이 아니므로 continue
        if len(w)==0 or int(w)<2:
            continue
        for i in range(2, int(int(w)**0.5)+1):
            if int(w)%i == 0:
                ck = False
                break
        if ck:
            answer += 1
    return answer

import sys
n, k = map(int, sys.stdin.readline().split())
print(solution(n, k))