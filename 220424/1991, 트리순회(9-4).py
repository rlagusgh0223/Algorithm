# 책에 있는것보다 이게 나한텐 더 쉽다
# 예전에 풀었던건데 기억하지 못했다
import sys

def preorder(data):
    if data != '.':
        print(data, end='')
        preorder(tree[data][0])
        preorder(tree[data][1])
def inorder(data):
    if data != '.':
        inorder(tree[data][0])
        print(data, end='')
        inorder(tree[data][1])
def postorder(data):
    if data != '.':
        postorder(tree[data][0])
        postorder(tree[data][1])
        print(data, end='')

N = int(sys.stdin.readline())
tree = {}
for i in range(N):
    data, left, right = sys.stdin.readline().split()
    tree[data] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')