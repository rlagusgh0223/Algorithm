# 길이가 더 짧거나 같은 A문자열의 앞과 뒤에 B문자열과 길이가 같도록 아무 알파벳이나 붙일 수 있다고 했으므로
# A문자열과 가장 차이가 적은 구간을 B문자열에서 찾으면 된다
# ex
# A = abcd
# B = abcdef
# B-A+1 = 3
# i = 0 ~ 2
# i가 0일때 (abcd)ef
# i가 1일때 a(bcde)f
# i가 2일때 ab(cdef)
# 위에서 A랑 ()안의 B가 가장 차이가 적은건 i가 0일때 이다
import sys
A, B = list(sys.stdin.readline().split())
ans = []
for i in range(len(B) - len(A) + 1):
    cnt = 0
    for j in range(len(A)):
        if B[i+j] != A[j]:
            cnt += 1
    ans.append(cnt)
print(min(ans))