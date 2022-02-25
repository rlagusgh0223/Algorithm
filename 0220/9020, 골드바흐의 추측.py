from math import sqrt
import sys

def prime(n):
    prime_num = [True] * n
    for i in range(2, int(sqrt(n)+1)):
        if prime_num[i] is True:
            for j in range(2*i, n, i):
                prime_num[j] = False

    return [i for i in range(2, n) if prime_num[i] is True]

p = prime(10001)    # 10001까지의 모든 소수를 p에 저장
n = int(sys.stdin.readline())
for i in range(n):
    m = int(sys.stdin.readline())
    diff = 10001
    a = 0
    b = 0
    for i in range(len(p)):
        if p[i] >= m/2:    # m/2부터 커지면서 m-p[i]가 소수인지 검사
            if m - p[i] in p:
                a = p[i]
                b = m - p[i]
                break
    print(b, a)



#================================================================
# 내가 풀었지만 시간초과
# from math import sqrt
# import sys

# def sosu(x):
#     lst = []    # 소수를 입력하는 리스트
#     result = []    # 소수의 합이 x와 같으면 입력하는 리스트
#     check = [True] * (x+1)    # 소수를 판단하기 위한 리스트
#     ans = 10000    # 리스트의 차를 확인하기 위한 변수. 입력을 10000까지라고 제한해서 10000을 줌

#     for i in range(2, int(sqrt(x)+1)):    # 소수인지 판별하는 반복문
#         if check[i]:
#             for j in range(i*2, x+1, i):    # 소수가 아니면 그 순서에 False를 넣는다
#                 check[j] = False
    
#     for i in range(2, x+1):    # 소수를 lst리스트에 입력. check를 입력된수+1개만큼 선언했으므로 check가 True인 자리수 그대로 넣으면 된다
#         if check[i]:
#             lst.append(i)

#     for i in range(len(lst)):
#         for j in range(i, len(lst)):    # 출력하는 소수는 작은것부터 출력해야 되니까 뒤쪽에 순서 바뀌는건 빼주기 위해 ex.) 3,7 이면 되지 7,3은 해당 안된다
#             if lst[i] + lst[j] == x:
#                 result.append([lst[i], lst[j]])

#     for i in range(len(result)):    # 리스트 중 각 리스트 값의 차가 최소인 값 확인
#         if ans > abs(result[i][1]-result[i][0]):
#             ans = abs(result[i][1]-result[i][0])    # 앞에 수가 더 작거나 같을테니 abs는 필요 없지만 혹시 몰라 준비
#             X = result[i][0]
#             Y = result[i][1]

#     return X, Y

# n = int(sys.stdin.readline())
# for i in range(n):
#     x, y = sosu(int(sys.stdin.readline()))
#     print(x, y)