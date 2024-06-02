def DFS(b, i, depth):
    if depth == 0:
        return True
    elif b[i] == '0':
        if b[i-depth]=='1' or b[i+depth]=='1':
            return False
    l = DFS(b, i-depth, depth//2)
    r = DFS(b, i+depth, depth//2)
    return l and r

def solution(numbers):
    answer = []
    for num in numbers:
        b = bin(num)[2:]  # 42 -> 101010
        node = bin(len(b)+1)[2:]  # 7 -> 111

        if '1' in node[1:]:
            dummy = (1<<len(node)) - int(node, 2)
            b = '0'*dummy + b
        
        result = DFS(b, len(b)//2, (len(b)+1)//4)
        answer.append(1 if result else 0)
    return answer

import sys

numbers = list(map(int, sys.stdin.readline().split(", ")))
print(solution(numbers))