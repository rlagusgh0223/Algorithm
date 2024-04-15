def solution(bin1, bin2):
    answer = ''
    # bin1을 이진수로 받아 십진수로 변환
    bin1 = int(bin1, 2)
    bin2 = int(bin2, 2)
    # bin() 함수는 결과를 이진수로 변환한다
    answer = bin(bin1+bin2)
    # 이진수는 0b로 시작하므로 앞의 두 글자는 빼고 리턴한다
    return answer[2:]

import sys

bin1 = sys.stdin.readline().strip()
bin2 = sys.stdin.readline().strip()
print(solution(bin1, bin2))