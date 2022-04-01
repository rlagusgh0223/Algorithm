import sys
A = int(sys.stdin.readline())
# cal = input()
cal = sys.stdin.readline().rstrip()    # rstrip()을 빼면 \n도 입력으로 받아서 아래 식이 돌아가지 않는다. input()은 원래 \n를 빼고 입력받기 때문에 잘 동작함
B = int(sys.stdin.readline())

if cal == '+':
    print(A+B)
elif cal == '*':
    print(A*B)