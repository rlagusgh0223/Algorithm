from collections import deque
import sys
s, t = map(int, sys.stdin.readline().split())
limit = 10 ** 9
q = deque()  # s에서 t까지 가는지, 간다면 어떤 연산을 통해 가는지 입력할 큐
q.append((s, ''))
check = set()  # 이미 계산한 수인지 체크하기 위한 set
check.add(s)
while q:
    s, operator = q.popleft()
    if s == t:
        if len(operator) == 0:  # 입력된 s가 t와 같은 경우
            operator = '0'
        print(operator)
        exit()
    # *를 위에 올려야 문제에서 요구한 답이 나온다
    if 0<=s*s<=limit and s*s not in check:
        q.append((s*s, operator+'*'))
        check.add(s*s)
    if 0<=s+s<=limit and s+s not in check:
        q.append((s+s, operator+'+'))
        check.add(s+s)
    if 0<=s-s<=limit and s-s not in check:
        q.append((s-s, operator+'-'))
        check.add(s-s)
    if s!=0 and 0<=s//s<=limit and s//s not in check:
        q.append((s//s, operator+'/'))
        check.add(s//s)
print(-1)