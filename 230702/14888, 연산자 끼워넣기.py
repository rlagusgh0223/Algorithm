def DFS(index, sumA):
    global maxA, minA
    # 모든 수를 다 계산했다면 그 값과 지금까지의 최댓값, 최소값을 비교한다
    if index == N-1:
        if maxA < sumA:
            maxA = sumA
        if minA > sumA:
            minA = sumA
    for i in range(4):
        temp = sumA
        # 연산하기로 한 수만큼 다 했다면 연산하지 않는다
        if operator[i] == 0:
            continue
        # 연산자를 반영하여 다음 수와 계산
        if i == 0:
            sumA += A[index+1]
        elif i == 1:
            sumA -= A[index+1]
        elif i == 2:
            sumA *= A[index+1]
        else:
            if sumA < 0:
                sumA = abs(sumA) // A[index+1] * -1
            else:
                sumA //= A[index+1]
        operator[i] -= 1
        DFS(index+1, sumA)
        operator[i] += 1
        sumA = temp

import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split())) # 중간에 연산자를 사용할 수
operator = list(map(int, sys.stdin.readline().split()))  # 덧셈, 뺄셈, 곱셈, 나눗셈을 몇 번 쓸지 입력하는 리스트
# 최댓값은 10억보다 작거나 같고, 최솟값은 10억보다 크거나 같다
# 초기값은 각각 반대로 max에 최솟값보다 작은 값을, min에 최댓값보다 큰 값을 주어 최댓값 최솟값을 계산할 수 있게 한다
maxA = -(10**10) - 1
minA = 10**10 + 1
DFS(0, A[0])  # 몇번째 수 인지, 그 문자까지의 합
print(maxA)
print(minA)