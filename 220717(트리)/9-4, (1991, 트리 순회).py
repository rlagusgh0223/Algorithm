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

N = int(input())
tree = {}
for i in range(N):
    now, left, right = input().split()
    tree[now] = [left, right]

preorder('A')
print()
inorder('A')
print()
postorder('A')