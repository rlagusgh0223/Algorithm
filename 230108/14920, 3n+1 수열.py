# 수열을 출력하라는게 아닌, 수열의 몇번째인지를 출력하라는 문제라 리스트를 만들 필요는 없어 보인다
import sys
C = int(sys.stdin.readline())
cnt = 1
while C != 1:
    cnt += 1
    if C%2 == 0:
        C //= 2
    else:
        C = 3*C + 1
print(cnt)