# 트라이 자료구조
class NODE:    # 트라이에 글자를 저장하는 노드
  def __init__(self):
    self.value = False    # 문자열의 끝 표시하기 위한 문자열
    self.childs = {}    # 문자열이 연결된 트리를 만들기 위해 노드의 데이터로 만듦

class Trie:
  def __init__(self):    # 트라이 자료구조에 루트노드를 만들어준다
    self.root = NODE()

  def insert(self, phone_num):    # 트라이 자료구조의 문자열을 삽입할 때의 알고리즘
    curNode = self.root    # 현재 노드를 트라이의 루트노드로 설정
    for num in phone_num:    # 전화번호의 글자 하나하나씩 탐색해가며
      if num not in curNode.childs:    # 현재 노드의 자식 중 전화번호의 글자가 없다면
        curNode.childs[num] = NODE()    # 현재 노드의 자식에 새로운 노드를 만든다
      curNode = curNode.childs[num]    # 현재 노드를 현재 노드의 자식 중 num으로 위치시킨다
      if curNode.value is True:    # 문제의 접두어 확인을 위한 알고리즘
        return False    # 현재 노드가 문자열의 끝이라면 접두어와 만난것이므로 False반환
    curNode.value = True    # 현재 노드는 문자열의 끝을 가리킨다. 문자열의 끝 노드는 True를 표시한다
    return True    # 접두어를 만나지 못했으므로 True 반환한다

for _ in range(int(input().rstrip())):
  n = int(input().rstrip())    # n과 전화번호 목록을 입력받는다
  phone_list = [input().rstrip() for _ in range(n)]
  phone_list.sort()    # 전화번호 목록을 길이가 짧은것부터 오게 한다
  trie = Trie()    # 트라이 자료구조를 트라이 클래스를 통해서 만듦
  tof = True    # 한 전화번호와 다른 전화번호의 접두어가 겹치는지 확인하는 변수
  for num in phone_list:    #전화번호 목록에 있는 전화번호를 하나하나 트라이에 삽입하며,
    tof = trie.insert(num)    # 이때 한 전화번호와 다른 전화번호의 접두어가 겹친다면 tof=False로 설정 후
    if not tof:
      break    # for문을 탈출한다
  if tof:    # tof = True라면 'YES'를 출력하고
    print('YES')
  else:    # False라면 NO를 출력한다
    print('NO')