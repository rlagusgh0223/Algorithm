def solution(keymap, targets):
    answer = []
    dic = {}
    for now in range(ord('A'), ord('Z')+1):
        dic[chr(now)] = 0
    
    # 각 번호가 몇번째인지 판단
    for key in keymap:
        for k in range(len(key)):
            if dic[key[k]] == 0:
                dic[key[k]] = k+1
            else:
                dic[key[k]] = min(dic[key[k]], k+1)

    # 각 단어별로 자판을 몇 번 눌러야 되는지 입력
    for target in targets:
        result = 0
        for t in target:
            result += dic[t]
            # 이번 단어에 대해 한 글자라도 자판에 없다면 글자를 작성할 수 없으므로
            # result를 -1로 만들고 더 이상 자판을 누르는 횟수를 세는 계산을 하지 않는다
            # 여기서 바로 return을 하면 다른 단어는 몇 번 누르면 되는지가 나오지 않으므로
            # 다른 단어에 대한 계산은 이어서 진행한다
            if dic[t] == 0:
                result = -1
                break
        answer.append(result)

    return answer


import sys
keymap = list(sys.stdin.readline().strip().split('", "'))
targets = list(sys.stdin.readline().strip().split('","'))
print(solution(keymap, targets))