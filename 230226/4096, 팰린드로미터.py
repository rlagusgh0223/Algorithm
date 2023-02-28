# zfill() : ()안의 자릿수만큼 문자열 앞에 0을 채워주는 함수
# 문자열 뒤에 붙여서 사용한다. ex) '문자열'.zfill(5) -> 00문자열
import sys
while True:
    N = sys.stdin.readline().rstrip()
    cnt = 0
    if N == '0':
        break
    elif N == N[::-1]:
        print(cnt)
        continue
    else:
        tmp = len(N)
        while N != N[::-1]:
            t = int(N) + 1
            N = str(t).zfill(tmp)
            cnt += 1
        print(cnt)
        continue