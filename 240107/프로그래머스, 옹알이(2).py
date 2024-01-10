def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for word in words:
            # 연속으로 두번 같은 말은 할 수 없다고 했으므로
            if word*2 not in bab:
                # 두번 연속만 아니라면 할 수 있는 단어 공백을 처리
                bab = bab.replace(word, ' ')
        # 모두 공백이면 True를 리턴하는 isspace를 통해
        # 모두 공백일 경우(모두 발음할 수 있는 경우) 발음 가능한 단어 1 추가
        if bab.isspace():
            answer += 1
    return answer

import sys
ba = list(sys.stdin.readline().strip().split('", "'))
print(solution(ba))