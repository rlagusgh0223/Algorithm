# for-else
# for문에서 break가 되지 않고 끝까지 반복을 실행했을 경우
# else에 있는 코드를 실행한다

# R이 나올때마다 reverse를 하면 시간초과가 나온다
# 카운터를 해서 홀수일 경우에만 reverse를 하고,
# 홀수일땐 뒤에서, 짝수일땐 앞에서 숫자를 지우게 한다

# 0이 되더라도 D가 없으면 error가 아니다

# 처음에 n이 0인 경우 []로 초기값을 넣어줘야 error가 나온다

from collections import deque
import sys
T = int(sys.stdin.readline())
for i in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    x = sys.stdin.readline()[1:-2].split(',')
    X = deque(x)
    flag = 0
    if n==0:
        X = []
    for j in p:
        if j == 'R':
            flag += 1
        elif j == 'D':
            if len(X)==0:
                print('error')
                break
            elif flag%2 == 0:
                X.popleft()
            else:
                X.pop()
    else:
        if flag%2 == 1:
            X.reverse()
            print('['+(',').join(X)+']')
        else:
            print('['+(',').join(X)+']')