# 처음 받은 문자열은 하나씩 비교하고
# 두번재 받은 문자열은 배열이라고 가정해서
# cache에 반영하는것 같은데 잘 모르겠다
import sys
word1 = sys.stdin.readline().rstrip()
word2 = sys.stdin.readline().rstrip()
l1, l2 = len(word1), len(word2)
cache = [0] * l2
for i in range(l1):
    cnt = 0
    for j in range(l2):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1
print(max(cache))