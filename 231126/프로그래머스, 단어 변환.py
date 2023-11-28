from collections import deque
def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    visit = [0] * len(words)
    while q:
        word, cnt = q.popleft()
        # target과 같은 단어가 나왔다면 연산 끝났다
        if word == target:
            answer = cnt
            break
        # 지금 순서의 단어를 모든 단어들과 비교한다
        # visit이 있으므로 자기 자신과 대조할 일은 없다
        for i in range(len(words)):
            diff = 0
            # 큐에 들어간 적인 없는 단어라면
            if visit[i] == 0:
                # 해당 단어와 리스트 안의 모든 단어들이 각각 다른 부분의 갯수를 구한다
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        diff += 1
                # 다른 부분이 한곳 뿐이라면
                # 큐에 단어와 cnt+1을 넣어준다. 단어 중 한 부분을 바꾼거다
                # visit[i]=1로 큐에 단어 넣었다고 표시해준다
                if diff == 1:
                    q.append([words[i], cnt+1])
                    visit[i] = 1
    return answer

import sys
b = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()
w = list(sys.stdin.readline().strip().split('", "'))
print(solution(b, t, w))