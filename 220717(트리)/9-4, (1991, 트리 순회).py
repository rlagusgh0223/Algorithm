import sys

def preorder(now):
    if now != '.':
        print(now, end='')
        preorder(tree[now][0])
        preorder(tree[now][1])

def inorder(now):
    if now != '.':
        inorder(tree[now][0])
        print(now, end='')
        inorder(tree[now][1])

def postorder(now):
    if now != '.':
        postorder(tree[now][0])
        postorder(tree[now][1])
        print(now, end='')
        
n = int(sys.stdin.readline())
tree = {}
for _ in range(n):
    middle, left, right = sys.stdin.readline().split()
    tree[middle] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')