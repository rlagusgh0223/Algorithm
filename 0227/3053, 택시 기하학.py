# 유클리드 기하학은 반지름이 주어졌을 때 원이 나오고
# 택시 기하학은 마름모 꼴이 나온다

import sys, math
n = int(sys.stdin.readline())
print("{:.6f}".format(n*n*math.pi))    # format은 {:.숫자f}를 쓰면 그 자리까지 출력하겠다는 의미 / 3.14쓰면 답 안나온다
print("{:.6f}".format(n*n*2))    # n의 길이의 밑변과 높이를 가진 직각 삼각형 4개의 넓이를 구하면 된다