# import sys, string
# alp = list(string.ascii_uppercase)
# pla = alp[::-1]
# ZOAC = sys.stdin.readline().rstrip()
# cnt = 0  # 총 시간
# n1, n2 = 0, -1  # 알파벳 순서
# for now in ZOAC:
#     sec = 0  # 몇 초 걸리는지
#     while True:
#         if alp[n1]==now:
#             cnt += sec
#             break
#         elif pla[n2]==now:
#             cnt += sec
#             break
#         n1, n2 = (n1+1) % 26, (n2+1) % 26
#         sec += 1
#     n1, n2 = alp.index(now), pla.index(now)
# print(cnt)



# 모범답안
import sys
word = list(sys.stdin.readline().rstrip())
start = 'A'
time = 0
for i in word:
    left = ord(i) - ord(start)  # 원판 왼쪽으로 돌리기
    right = ord(start) - ord(i)  # 원판 오른쪽으로 돌리기
    if left < 0:
        left += 26
    if right < 0:
        right += 26
    time += min(left, right)
    start = i
print(time)