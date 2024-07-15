from collections import deque


def solution(begin, target, words):
    q = deque()
    q.append((begin, 0))
    visit = [0] * len(words)
    while q:
        word, cnt = q.popleft()
        # 목표한 단어가 되면 변환 횟수 리턴한다
        if word == target:
            return cnt
        for i in range(len(words)):
            if visit[i] == 0:
                check = 0
                # 모든 단어들은 단어의 길이가 같으므로
                # 한 글자씩 비교할 수 있다
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        check += 1
                # 한 글자만 다른 경우 해당 단어로
                # 변환했다고 가정하고 q에 입력한다
                # 이때 변환 횟수도 1 늘려준다
                # 한 글자만 다를때만 입력하는 이유는
                # 한 번에 한 글자만 바꿀 수 있다고
                # 문제에서 주어졌기 때문이다
                if check == 1:
                    q.append((words[i], cnt+1))
                    # 한 번 입력한 단어를 다시 입력하지 않도록
                    # 입력한 단어라고 표시한다
                    visit[i] = 1
    # 변환할 수 없는 경우 0을 리턴한다
    return 0


import sys

begin, target = sys.stdin.readline().split()
words = list(sys.stdin.readline().strip().split('", "'))
print(solution(begin, target, words))