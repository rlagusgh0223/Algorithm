# replace() : 왼쪽부터 해당하는 문자열을 찾아서 치환
# 단, 리스트로 입력 받으면 replace함수는 동작하지 않는다
import sys
board = sys.stdin.readline().rstrip()
board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")
if 'X' in board:
    print(-1)
else:
    print(board)

# import sys
# board = list(sys.stdin.readline().rstrip())
# ans = []
# cnt = 1
# for i in range(len(board)):
#     if board[i]=='.' or i==len(board)-1:
#         if board[i] == '.':
#             cnt -= 1
#         if cnt%4 == 0:
#             ans +='AAAA'*(cnt//4)
#             cnt = 0
#         elif cnt%4 == 2:
#             ans += 'AAAA'*(cnt//4) + 'BB'
#             cnt = 0
#         else:
#             print(-1)
#             exit()
#         if board[i] == '.':
#             ans += '.'
#     cnt += 1
# print(*ans, sep='')