def solution(storey):
    answer = 0
    while storey:
        st = storey % 10
        # 6 ~ 9
        # 6~9층일땐 1층씩 올라가 10층 단위로 맞춘다
        if st > 5:
            answer += (10 - st)
            storey += 10
        # 0 ~ 4
        # 0~4층일땐 1층씩 내려가 10층 단위로 맞춘다
        elif st < 5:
            answer += st
        # 5
        # 5층일땐 그 앞의 자릿수(10의자리)의 값이 5~9면 10층 올라가고
        # 0~4이면 0으로 간다
        else:
            if (storey//10)%10 > 4:
                storey += 10
            answer += st
        storey //= 10
    return answer

import sys
storey = int(sys.stdin.readline())
print(solution(storey))