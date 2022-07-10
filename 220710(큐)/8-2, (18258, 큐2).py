from collections import deque
import sys
N = int(sys.stdin.readline())
queue = deque()

def push(x):
    return queue.append(x)
def pop():
    if queue:
        return queue.popleft()
    else:
        return -1
def size():
    return len(queue)
def empty():
    if queue:
        return 0
    else:
        return 1
def front():
    if queue:
        return queue[0]
    else:
        return -1
def back():
    if queue:
        return queue[-1]
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
    elif command[0] == 'front':
        print(front())
    elif command[0] == 'back':
        print(back())