def back_Tracking(index ,sum):
    global minAns, maxAns
    if index==N-1:    # 백트랭킹 함수 핵심. 인덱스가 n-1이라면 마지막 인덱스에 접근했다는 뜻이고, 함수를 종료해야된다.
        if minAns > sum:    # sum을 통해 최댓값, 최솟값을 갱신
            minAns = sum
        if maxAns < sum:
            maxAns = sum
        return

    for i in range(4):    # 덧셈, 뺄셈, 곱셈, 나눗셈 4가지 경우를 탐색하기 위한 for문
        temp = sum    # 임시적으로 sum값을 저장하기 위한 temp변수 초기화
        if operator[i] == 0:    # operator[i]==0이면 해댱 연산자는 더 이상 남아있지 않으므로 continue
            continue
        if i==0:    # 연산자가 덧셈이라면 sum에 다음 인덱스 값을 더해준다
            sum += numArr[index+1]
        elif i==1:    # 연산자가 뺄셈이라면 sum에 다음 인덱스 값을 빼준다
            sum -= numArr[index+1]
        elif i==2:    # 연산자가 곱셈이라면 sum에 다음 인덱스 값을 곱해준다
            sum *= numArr[index+1]
        else:    # 연산자가 나눗셈이라면 sum에 다음 인덱스 값을 나누어 준다
            if sum<0:    # 음수 나눗셈
                sum = abs(sum)//numArr[index+1]*-1
            else:
                sum //= numArr[index+1]

        operator[i] -= 1    # 해당 연산자는 사용했으므로, operatro[i]값을 1빼준다. 0이면 연산자를 모두 사용했다는 의미
        back_Tracking(index+1, sum)    # 연산자를 1개 사용한 채로 back_Tracking(index+1, sum)을 실행. 이는 현재의 다음 인덱스와 지금까지 더한 sum을 넘겨준다
        operator[i] += 1    # operator[i]값을 1 증가시킨다. 연산자를 다시 선택하지 않은 상태로 만들기 위함이다.
        sum = temp    # sum값을 다시 원래 sum값 temp로 바꿔준다.

N = int(input())
numArr = list(map(int, input().split()))
operator = list(map(int, input().split()))
minAns = float('Inf')    # 최솟값을 저장하기 위한 변수를 -무한으로 설정
maxAns = float('-Inf')

back_Tracking(0, numArr[0])
print(maxAns)
print(minAns)