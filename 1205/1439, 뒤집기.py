"""
import sys
s = list(map(int,sys.stdin.readline().rstrip()))
cnt = 0

for i in range(len(s)-1):
    #0->1 이나 1->0인 경우에만 cnt += 1을 해준다
    if s[i] != s[i+1]:
        cnt += 1

#0 또는 1 중 하나만 바꾸면 되기 때문에 //2를 해준다
print(cnt//2)
"""
import sys
s = list(map(int, sys.stdin.readline().rstrip()))

cnt0 = 0    # 0 -> 1의 갯수 카운트 변수
cnt1 = 0    # 1 -> 0의 갯수 카운트 변수

#연산이 한번만 일어날 경우 0이 출력되는것 방지
#ex. 0000001이면 cnt0=1이고 cnt1=0이라서 0이 나온다
if s[0] == 0:   #첫번째 수가 0인경우
    cnt1 += 1    # 1 -> 0이 되는 경우를 하나 더해준다
else:   ##첫번째 수가 1인경우
    cnt0 += 1    # 0 -> 1이 되는 경우를 하나 더해준다

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == 0: # 0 -> 1
            cnt0 += 1
        else:         # 1 -> 0
            cnt1 += 1

print(min(cnt0, cnt1))
