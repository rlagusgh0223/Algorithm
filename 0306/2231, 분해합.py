import sys
n = int(sys.stdin.readline())
result = 0

for i in range(1, n+1):    # 1부터 n까지
    a = list(map(int, str(i)))    # 각 자리 수를 분해
    result = i + sum(a)    # 그대로인 값 i와 분해한 각 자리수의 합
    if result == n:    # 만약 분해합이 n과 같다면
        print(i)    # 그 자리에서 종료, 작은값부터 하라고 했으니 1에서부터 시작
        break
    if i == n:    # 생성자가 없는 경우
        print(0)