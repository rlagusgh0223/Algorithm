# permutations를 쓰면 리스트에서 몇개를 뽑을지 정할 수 있다
from itertools import permutations
import sys
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
card = [sys.stdin.readline().rstrip() for _ in range(n)]
ans = set()
for now in permutations(card, k):
    ans.add(''.join(now))
print(len(ans))



# import sys
# n = int(sys.stdin.readline())
# k = int(sys.stdin.readline())
# lst = [sys.stdin.readline().rstrip() for _ in range(n)]
# ans = []
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             continue
#         if k==2:
#             ans.append(int(lst[i]+lst[j]))
#         else:
#             for kk in range(n):
#                 if i==kk or j==kk:
#                     continue
#                 if k==3:
#                     ans.append(int(lst[i]+lst[j]+lst[kk]))
#                 else:
#                     for l in range(n):
#                         if i==l or j==l or kk==l:
#                             continue
#                         ans.append(int(lst[i]+lst[j]+lst[kk]+lst[l]))
# print(len(set(ans)))