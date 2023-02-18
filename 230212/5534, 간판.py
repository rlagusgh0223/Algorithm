# 동일한 간격으로 간판의 글자가 써있어야 하므로 첫글자와 끝글자의 위치를 구하고 중간값을 비교한다
def check(gp):
    l = len(gp)
    for start in range(l):
        if gp[start] == ans[0]:
            for end in range(start, l):
                if gp[end] == ans[-1]:
                    avg = (end-start)//(n-1)
                    cnt = 0
                    while cnt < n:
                        if gp[start+avg*cnt] == ans[cnt]:
                            cnt += 1
                        else:  # 이번 start에서는 짝이 안 맞은 경우 다음 start를 찾아본다
                            break
                    else:  # cnt==n인 경우, 즉 모든 문자가 맞는 경우
                        return 1
    return 0

import sys
N = int(sys.stdin.readline())
ans = list(sys.stdin.readline().rstrip())
n = len(ans)
ganpan = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
cnt = 0
for gp in ganpan:
    cnt += check(gp)
print(cnt)