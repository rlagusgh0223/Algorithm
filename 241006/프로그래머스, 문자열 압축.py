# 예시
# 입력: "aabbaccc"
# 압축 1단위: "aabbaccc" → 그대로 "aabbaccc" (길이: 8)
# 압축 2단위: "aa", "bb", "ac", "cc" → "2a2ba3c" (길이: 7)
# 압축 3단위: "aab", "bac", "cc" → "aabbaccc" (길이: 8)
# 압축 4단위: "aabb", "accc" → "aabbaccc" (길이: 8)
# 최종 결과는 2단위로 압축된 문자열이 가장 짧으며, 길이는 7입니다.
def solution(s):
    answer = len(s)

    # 길이가 1이면 더 길이 그대로 리턴
    if answer == 1:
        return answer
    
    # 1부터 문자열 절반까지 압축 시도
    for step in range(1, len(s)//2+1):
        cnt = 1  # 문자열의 반복 횟수
        word = ''  # 압축한 문자열
        now = s[:step]  # 이번 문자열

        # 압축한 길이만큼 문자열 선회(0~step은 이미 word에 입력했다)
        for i in range(step, len(s), step):
            # 이번 문자열과 동일하다면 cnt만 1 증가
            if now == s[i:i+step]:
                cnt += 1
            # 이번 문자열과 다르다면
            else:
                # cnt가 2 이상인 경우 숫자를 문자열 앞에 붙이고
                # 그렇지 않다면 cnt없이 문자열만 압축한 문자열에 붙인다
                if cnt > 1:
                    word += str(cnt)+now
                else:
                    word += now
                # 이번 문자열을 바꾸고 cnt를 다시 1로 한다
                cnt = 1
                now = s[i:i+step]
        # 문자열이 나누어 떨어지지 않는다면 마지막 문자열이 포함되지 않았으므로 포함한다
        # 문자열이 정확히 나누어 떨어지더라도 반복 패턴이 있을 수 있다
        # 그러므로 항상 마지막 패턴을 처리해야 한다
        if cnt > 1:
            word += str(cnt)+now
        else:
            word += now
        # 압축한 결과 가장 짧은 문자열의 길이를 구한다
        answer = min(answer, len(word))
    return answer

import sys

print(solution(sys.stdin.readline().strip()))
