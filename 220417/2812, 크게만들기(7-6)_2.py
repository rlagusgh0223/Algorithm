# 내 나름대로 다시 풀어본 풀이. 그런데 틀렸다고 나온다
import sys
N, K = map(int, sys.stdin.readline().split())
number = list(sys.stdin.readline().rstrip())    # 밑에서 join은 int는 안되고 string만 된다고 해서 int로 안했다

answer = []
cnt = K
for num in number:
    while answer and cnt>0 and answer[-1]<num:
        del answer[-1]
        cnt -= 1
    answer.append(num)
print(''.join(answer))
#print(''.join(answer[:N-K]))    # 이렇게 하면 맞았다고 나온다
# 어차피 위에서 지워서 똑같은데 뭐가 다른건지 모르겠다


###########################################
# 모범답안
import sys
N, K = map(int, sys.stdin.readline().split())
number = list(sys.stdin.readline())

answer = []    # 스택으로 이용할 answer변수 생성
cnt = K
for num in number:    # number 배열 순회
    # answer 리스트가 비어있지 않고, 지울 수 있는 횟수가 남아있고,
    # answer의 마지막 값(지워지지 않은 현재와 가장 가까운 앞의 수)이 num(현재 순회하는 값)보다 작다면 answer의 마지막 값을 지운다.
    while answer and cnt>0 and answer[-1]<num:
        del answer[-1]
        cnt -= 1
    answer.append(num)

print(''.join(answer[:N-K]))