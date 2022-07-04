import sys
stack = []
N = int(sys.stdin.readline())

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
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        push(order[1])
    elif order[0] == 'pop':
        print(pop())
    elif order[0] == 'size':
        print(size())
    elif order[0] == 'empty':
        print(empty())
    elif order[0] == 'top':
        print(top())