def backTracking(index, sum):    # 함수의 인자로(인덱스, 지금까지 더한 값)을 받는다
    # print("index = ", index, "sum = ", sum)
    global minAns, maxAns    # 최솟값, 최댓값을 저장하기 위한 변수를 전역변수로 생성한다
    if index == N-1:    # 함수의 끝
        if minAns > sum:
            minAns = sum
        if maxAns < sum:
            maxAns = sum
        
    for i in range(4):    # 덧셈, 뺄셈, 곱셈, 나눗셈을 구하기 위한 반복문
        temp = sum    # 일시적으로 sum값을 저장하기 위한 temp 변수 초기화
        if operator[i]==0:    # 연산자는 더이상 존재하지 않으므로 이번 턴 종료
            continue

        # 이 밑으로는 1 이상, 즉 연산자가 있다는 소리 - 덧셈(0), 뺄셈(1), 곱셈(2), 나눗셈(3)
        if i == 0:
            sum += numArr[index+1]
        elif i == 1:
            sum -= numArr[index+1]
        elif i == 2:
            sum *= numArr[index+1]
        else:
            if sum < 0:    # C++기준으로 음수 나눗셈을 진행하라고 했으므로 sum의 절댓값과 현재 수를 나눈 후 -1을 곱했다(sum이 음수니까)
                sum = abs(sum) // numArr[index+1] * -1
            else:
                sum //= numArr[index+1]    # sum이 양수인 경우에는 그냥 나눈 몫만 구하면 된다

        operator[i] -= 1    # 해당 연산자는 사용했으므로, 1을  빼준다(ex. 덧셈 2 -> 1)
        # print("재귀 전 : ", operator)
        backTracking(index+1, sum)    # 연산자를 1개 사용한채로 다음 인덱스와 지금까지 더한 sum을 넘겨준다
        operator[i] += 1    # 연산자 원 상태 복구. 이걸 해야 다음 계산에서 돌아간다
        # print("재귀 후 : ", operator)
        sum = temp    # for문 다음 i에도 sum값을 함수의 인자로 받은 값으로 다시 쓰기 위해 temp값 sum에 넘겨준다

N = int(input())
numArr = list(map(int, input().split()))
operator = list(map(int, input().split()))
minAns = float('Inf')    # min을 -무한으로 설정 <- 어차피 나머지 없이 몫만 연산해서 정수가 나올텐데 실수 쓸 필요가 있나?
maxAns = float('-Inf')

backTracking(0, numArr[0])    # 인덱스, 입력 받은 수의 첫값을 넘겨준다
print(maxAns)
print(minAns)