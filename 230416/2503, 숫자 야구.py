# 인터넷에 있는거보다 시간이나 메모리는 더 필요할지 몰라도 이게 더 직관적이라 이렇게 바꿨다
from itertools import permutations
import sys
lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
data = list(permutations(lst, 3))  # lst의 값들 중 3개가 되는 모든 값들을 data에 입력한다

N = int(sys.stdin.readline())
ck = [0] * len(data)  # 해당되는 수인지 아닌지 판단하기 위한 리스트
for _ in range(N):
    now, s, b = map(int, sys.stdin.readline().split())
    now = list(str(now))
    for i in range(len(data)):
        strike = ball = 0
        for j in range(3):
            if ck[i]==0 and data[i][j]==now[j]:
                strike += 1
            elif ck[i]==0 and now[j] in data[i]:
                ball += 1
        if strike!=s or ball!=b:  # 이번 수가 스트라이크나 볼의 수와 맞지 않는다면 아예 가망이 없으므로
            ck[i] = 1  # 이 수배열은 아니라고 표시
print(ck.count(0))