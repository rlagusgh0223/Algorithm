import sys
N = int(sys.stdin.readline())
stack = []
def push(x):
    return stack.append(x)
def pop():
    if stack:
        return stack.pop()
    else:
        return -1
def size():
    return len(stack)
def empty():
    if stack:
        return 0
    else:
        return 1
def top():
    if stack:
        return stack[-1]
    else:
        return -1

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        print(pop())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'top':
        print(top())