# replace 함수
# 문자열을 변경하는 함수
# replace(현재 문자열에서 변경하고 싶은 문자, 새로 바꿀 문자, 바꿀 횟수)
# 바꿀 횟수는 따로 입력하지 않으면 기본적으로 전체를 변경한다

import sys
A, B = sys.stdin.readline().split()
abmin = int(A.replace('6', '5')) + int(B.replace('6', '5'))
abmax = int(A.replace('5', '6')) + int(B.replace('5', '6'))
print(abmin, abmax)