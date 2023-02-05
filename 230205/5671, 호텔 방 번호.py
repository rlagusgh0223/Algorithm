# 암만 봐도 문제가 잘못된 것 같다
# EOFError로 except를 잡으면 입력 없을때 정지하는거라는데 런타임 에러 나오고
# 그냥 except로 해야 맞았다고 한다
import sys
while True:
    try:
        N, M = map(int, sys.stdin.readline().split())
        cnt = 0
        for room in range(N, M+1):
            ck1 = str(room)
            ck2 = set(ck1)
            if len(ck1) == len(ck2):
                cnt += 1
        print(cnt)
    except:
        break