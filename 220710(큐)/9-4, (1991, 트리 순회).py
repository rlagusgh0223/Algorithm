# 기존에 했던 방식이 더 쉬우므로 그 방식대로 하되, 책의 모범답안을 쓰도록 한다
class Node:
    def __init__(node, data, left_node, right_node):
        node.data = data
        node.left_node = left_node
        node.right_node = right_node

def pre_order(node):
    print(node.data, end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node !='.':
        pre_order(tree[node.right_node])

def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != '.':
        in_order(tree[node.right_node])

def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')

N = int(input())
tree = {}

for _ in range(N):
    data, left_node, right_node = input().split()
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])