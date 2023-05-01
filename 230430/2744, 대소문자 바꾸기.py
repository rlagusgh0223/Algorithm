import sys
N = list(sys.stdin.readline().rstrip())
for i in range(len(N)):
    if ord(N[i])>=97:
        N[i] = chr(ord(N[i]) - 32)
    else:
        N[i] = chr(ord(N[i]) + 32)
print(*N,sep='')


# 문제에서 이런 함수를 쓰는걸 바란건 아니겠지만 이런게 있다는건 알아둬라
# import sys
# S = sys.stdin.readline().rstrip()
# print(S.swapcase())  # 대소문자 변환해주는 함수