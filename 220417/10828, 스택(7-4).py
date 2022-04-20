import sys
N = int(sys.stdin.readline())
arr = []
stack = []

for i in range(N):
    arr.append(list(sys.stdin.readline().split()))

for i in range(N):    # 원래는 하나의 반복문에 넣어도 되지만 구분하기 위해 따로 만들었다
    if arr[i][0] == 'push':    # push는 스택에 입력
        stack.append(int(arr[i][1]))
    elif arr[i][0] == 'pop':    # pop은 아무것도 없으면 -1 출력, 있으면 맨 마지막에 입력한 수 제거 후 출력
        if stack:
            print(stack.pop())
        else:
            print("-1")
    elif arr[i][0] == 'size':    # size는 스택 크기 출력
        print(len(stack))
    elif arr[i][0] == 'empty':    # empty는 스택이 있으면 0, 없으면 1 출력
        if stack:
            print('0')
        else:
            print('1')
    elif arr[i][0] == 'top':    # top은 스택이 있으면 가장 마지막에 입력한 수, 없으면 -1 출력한다
        if stack:
            print(stack[-1])
        else:
            print("-1")