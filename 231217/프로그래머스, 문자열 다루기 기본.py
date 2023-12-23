def solution(s):
    # str.isdigit()  : 문자열이 숫자로만 이루어져 있는지 확인하는 함수
    return s.isdigit() and len(s) in [4, 6]

# 내 풀이
#def solution(s):
#    if len(s)!=4 and len(s)!=6:
#        return False
#    for now in s:
#        if "0"<=now<="9":
#            continue
#        return False
#    return True


import sys
s = sys.stdin.readline().strip()
print(solution(s))