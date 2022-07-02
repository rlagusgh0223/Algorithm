import sys
N = int(sys.stdin.readline())
Stack = []
for i in range(N):
    inS = sys.stdin.readline().split()
    if inS[0] == 'push':
        Stack.append(inS[1])
    elif inS[0] == 'pop':
        if Stack:
            print(Stack.pop())
        else:
            print(-1)
    elif inS[0] == 'size':
        print(len(Stack))
    elif inS[0] == 'empty':
        if Stack:
            print(0)
        else:
            print(1)
    elif inS[0] == 'top':
        if Stack:
            print(Stack[-1])
        else:
            print(-1)