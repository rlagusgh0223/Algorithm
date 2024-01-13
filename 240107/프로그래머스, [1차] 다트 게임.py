def solution(dartResult):
    answer = []
    # 숫자가 입력될때 10을 cnt에 곱하게 했으므로 초기값 0을 준다
    cnt = 0
    for now in dartResult:
        # isnumeric을 통해 문자열에서 숫자가 나오면 cnt값을 더한다
        # 숫자는 0에서 10까지라고 했으므로 10이 나올 경우를 대비해서 기존 값에 10을 곱하고 지금 값을 더한다
        # 한자리 숫자일땐 어차피 cnt가 0이므로 10을 곱해도 값이 변하지 않는다
        if now.isnumeric():
            cnt = cnt*10 + int(now)
            continue
        if now == 'S':
            answer.append(cnt)
        elif now == 'D':
            answer.append(cnt**2)
        elif now == 'T':
            answer.append(cnt**3)
        elif now == '*':
            answer[-1] *= 2
            if len(answer) > 1:
                answer[-2] *= 2
        elif now == '#':
            answer[-1] *= -1
        # 여기까지 계산이 끝났으면 하나의 문자열 세트가 끝났으므로 cnt값을 0으로 초기화 해준다
        cnt = 0
    return sum(answer)



import sys
dart = sys.stdin.readline().strip()
print(solution(dart))