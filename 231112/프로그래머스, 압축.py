# 현재 문자열 + 다음 문자 가 리스트에 있다면
# end += 1
# 현재 문자열 + 다음 문자 가 리스트에 없다면
# start = end, end += 1

def solution(msg):
    answer = []
    # A ~ Z 까지 1 ~ 26을 붙인 딕셔너리를 만든다
    word = {chr(ord('A')+i) : i+1 for i in range(26)}
    start, end = 0, 0  # 확인할 문자열의 시작 위치, 끝 위치
    while end < len(msg):
        end += 1
        # 해당 문자열이 저장된 리스트에 없다면
        if msg[start:end+1] not in word:
            # 저장된 리스트에 해당 문자열을 다음 번호를 붙여서 저장한다
            word[msg[start:end+1]] = len(word) + 1
            # 저장된 리스트에 있는 문자열의 번호를 answer에 입력한다
            answer.append(word[msg[start:end]])
            start = end
    # 조건이 end < len(msg)이기 때문에 마지막 문자를 검색하지 않으므로 answer에 입력을 추가해준다
    # 그렇다고 end <= len(msg)로 하면 word에 있는 문자열일 경우 answer에 들어가지 않는다
    # 리스트 길이보다 많은 범위를 지정하는건 에러가 뜨지 않는것 같다
    answer.append(word[msg[start:end]])
    return answer

import sys
msg = sys.stdin.readline().strip()
print(solution(msg))