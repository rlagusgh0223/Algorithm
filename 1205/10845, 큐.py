from collections import deque
import sys
queue = deque()

n = int(sys.stdin.readline())
for i in range(n):
    word = list(sys.stdin.readline().split())
    #print(word)
    if word[0] == 'push':
        queue.append(int(word[1]))

    elif word[0] == 'pop':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue.popleft())

    elif word[0] == 'size':
        print(len(queue))

    elif word[0] == 'empty':
        if len(queue) == 0:
            print('1')
        else:
            print('0')
        print(queue.empty)

    elif word[0] == 'front':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[0])

    elif word[0] == 'back':
        if len(queue) == 0:
            print('-1')
        else:
            print(queue[-1])
