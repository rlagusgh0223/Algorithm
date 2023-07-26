import sys
# 2진수로 입력한 숫자 10진수로 변환해서 받기
N = int(sys.stdin.readline(), 2)
# 17 곱하기
result = N * 17
# 10진수를 2진수로 출력(맨 앞의 두글자는 0b가 나오므로 제외한다)
print(bin(result)[2:])