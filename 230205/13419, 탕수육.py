# 시간과 메모리는 똑같다
import sys
T = int(sys.stdin.readline())
words = [sys.stdin.readline().rstrip() for _ in range(T)]
for word in words:
    if len(word)%2 == 0:
        print(word[::2])
        print(word[1::2])
    else:
        print(word[::2],word[1::2], sep='')
        print(word[1::2],word[::2], sep='')



# import sys
# T = int(sys.stdin.readline())
# for _ in range(T):
#     word = list(sys.stdin.readline().rstrip())
#     one, two = '', ''
#     for i in range(len(word)):
#         if i%2 == 0:
#             one += word[i]
#         else:
#             two += word[i]
#     if len(word)%2 == 1:
#         one, two = one+two, two+one
#     print(one)
#     print(two)