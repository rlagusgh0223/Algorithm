# 봐도 뭐가 뭔지 모르겠다
# 트리는 나중에 더 봐야될 것 같다
import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline
class Node:                         # 노드를 만들기 위한 클래스 정의
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    
    def add(self, data):            # 전위 순회에 각 입력에 대하여
        if self.root == None:
            self.root = Node(data)

        else:
            current = self.root
            while True:
                if current.data > data:             # 입력 데이터가 current 위치값보다 작다면
                    if current.left == None:        # current의 왼쪽이 비어 있으면 입력값을 current의 왼쪽에 넣는다
                        current.left = Node(data)
                        break
                    current = current.left          # 비어 있지 않다면 current값을 current의 왼쪽 자식 노드 위치로 옮기고 반복문으로 돌아간다
                if current.data < data:             # 입력 데이터가 current 위치값보다 크다면
                    if current.right == None:       # current의 오른쪽이 비어 있으면 입력값을 current의 오른쪽에 넣는다
                        current.right = Node(data)
                        break
                    current = current.right         # 비어 있지 않다면 current값을 current의 오른쪽 자식 노드 위치로 옮기고 반복문으로 돌아간다 

    def postOrder(self, node=None):                 # 만든 트리에 대한 후위 순회 함수
        global answer
        if node == None:
            node = self.root

        if node.left != None:
            self.postOrder(node.left)
        if node.right != None:
            self.postOrder(node.right)
        answer.append(node.data)

tree = Tree()
while True:             # 전위 순회 입력을 한 줄씩 입력받는다
    try:
        tree.add(int(sys.stdin.readline()))
    except:
        break
answer = []
tree.postOrder()        # 후위 순회 함수 실행
print("\n".join(map(str, answer)))