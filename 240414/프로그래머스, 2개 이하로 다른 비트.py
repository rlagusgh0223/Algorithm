def solution(numbers):
    answer = []
    for number in numbers:
        # 해당 숫자를 이진수로 바꾼 값을 입력한 변수
        # bin() 함수는 십진수를 이진수로 만들어준다
        num = list('0' + bin(number)[2:])
        
        # rfind() : ()안의 문자가 오른쪽에서부터 언제 처음 나오는지 출력해주는 함수
        # 짝수든 홀수는 지금 수 보다 크면서 2개 비트 이하로 다른 수는
        # 가장 마지막의 0을 1로 바꿔줘야 한다
        # 그 위치를 찾아서 idx에 넣어준다
        idx = ''.join(num).rfind('0')
        
        num[idx] = '1'
        # 짝수는 마지막 0만 바꿔주면 되지만
        # ex) 2(0010) -> 3(0011)
        # 홀수는 그 다음 수를 1로도 만들어 줘야 한다
        # ex) 7(0111) -> 11(1011)
        if number % 2 == 1:
            num[idx+1] = '0'
        answer.append(int(''.join(num), 2))
    return answer

import sys

numbers = list(map(int, sys.stdin.readline().split(",")))
print(solution(numbers))
