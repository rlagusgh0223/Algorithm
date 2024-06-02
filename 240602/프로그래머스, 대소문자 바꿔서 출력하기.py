import sys

str = sys.stdin.readline().strip()
answer = ''
for s in str:
    if ord('A')<=ord(s)<=ord('Z'):
        answer += s.lower()
    else:
        answer += s.upper()
print(answer)

# 모범답안
# import sys
# print(sys.stdin.readline().strip().swapcase())
# print(input().swapcase())