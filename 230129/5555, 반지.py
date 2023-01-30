# 코드는 이게 더 간단하지만 시간이나 메모리는 똑같다
import sys
word = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline())
cnt = 0
for _ in range(N):
    now = sys.stdin.readline().rstrip()
    now += now
    if word in now:  # now*2로 해도 동일한 결과가 나오는 ㅓㄳ 같다
        cnt += 1
print(cnt)


# import sys
# word = sys.stdin.readline().rstrip()
# N = int(sys.stdin.readline())
# cnt = 0
# for _ in range(N):
#     now = sys.stdin.readline().rstrip()
#     for i in range(len(now)):
#         for j in range(len(word)):
#             n = (i + j)%len(now)
#             ck = True
#             if now[n] == word[j]:
#                 ck = False
#             if ck:
#                 break
#         if not ck:
#             cnt += 1
#             break
# print(cnt)