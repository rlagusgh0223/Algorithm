# 정규 표현식 모듈을 가져온다
import re


def solution(files):
    # 각 파일명을 정규 표현식을 사용하여 숫자 부분과 그 외의 문자 부분으로 분리한다
    # ([0-9]+) 는 하나 이상의 숫자를 의미한다
    answer = [re.split(r"([0-9]+)", file) for file in files]
    
    # 분리된 파일명을 정렬한다
    # x[0].lower() : 파일명의 첫 번째 부분(문자 부분)을 소문자로 변환하여 사전 순으로 정렬
    # int(x[1]) : 파일명의 두 번째 부분(숫자 부분)을 정수로 변환하여 숫자 크기에 따라 정렬
    answer = sorted(answer, key=lambda x:(x[0].lower(), int(x[1])))
    
    # 정렬된 각 파일명을 문자열로 다시 조합
    return [''.join(file) for file in answer]

import sys

files = list(sys.stdin.readline().strip().split('", "'))
print(solution(files))
