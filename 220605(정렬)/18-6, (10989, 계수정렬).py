# 계수정렬
import sys
N = int(sys.stdin.readline())
lst = [0] * 10001    # 입력받을 수 있는 수 만큼 배열을 만든다(각 수의 입력받은 횟수를 측정)
for i in range(N):    # 입력받은 수에 대한 배열의 개수를 1 증가한다
    lst[int(sys.stdin.readline())] += 1

for i in range(len(lst)):
    if lst[i] != 0:    # 1번이라도 입력을 받았다면
        for j in range(lst[i]):    # 입력받은 횟수만큼 그 수 출력
            print(i)