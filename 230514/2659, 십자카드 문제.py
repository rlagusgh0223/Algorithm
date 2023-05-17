# 시계수로 검사할 4자리 문자열을 받으면 그 중에서 가장 작은값으로 계산한다
def clock(lst):
    tmp = int(''.join(lst))
    for i in range(4):
        now = int(''.join(lst[i:]+lst[:i]))
        if tmp > now:
            tmp = now
    return tmp

import sys
lst = list(sys.stdin.readline().split())
clk = clock(lst)
cnt = 0
for i in range(1111, clk+1):
    if '0' not in list(str(i)) and i==clock(list(str(i))):
        cnt += 1
print(cnt)