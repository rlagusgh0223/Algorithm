import sys
S = sys.stdin.readline().rstrip()
ans = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        ans.add(S[i:j+1])
print(len(ans))

# ababc에 대한 S[i:j+1]
# a
# ab
# aba
# abab
# ababc
# b
# ba
# bab
# babc
# a
# ab
# abc
# b
# bc
# c
# i부터 끝까지 모든 문자열을 입력하는데 set(집합)이므로
# 중복된 문자열은 받지 않는다
# i는 하나씩 증가하므로 출발 위치도 하나씩 증가한다