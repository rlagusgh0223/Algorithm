# 트라이 자료구조
class NODE:
  def __init__(self):
    self.value = False
    self.childs = {}

class Trie:
  def __init__(self):
    self.root = NODE()

  def insert(self, phone_num):
    curNode = self.root
    for num in phone_num:
      if num not in curNode.childs:
        curNode.childs[num] = NODE()
      curNode = curNode.childs[num]
      if curNode.value is True:
        return False
    curNode.value = True
    return True

for _ in range(int(input())):
  n = int(input())
  phone_list = [input() for _ in range(n)]
  phone_list.sort()
  trie = Trie()
  tof = True
  for num in phone_list:
    tof = trie.insert(num)
    if not tof:
      break
  if tof:
    print('YES')
  else:
    print('No')