def solution(n, lost, reserve):
    student = [1]*n
    for l in lost:
        student[l-1] -= 1
    for r in reserve:
        student[r-1] += 1
    for i in range(n):
        # 앞부분(i-1) 검사하는게 먼저 나와야 한다
        # 뒤(i+1)부터 검사하면 실패 나온다
        # 앞에 체육복이 필요한데 뒤에 먼저 줘버리면 앞에 주지 못하지만
        # 뒤는 그 다음사람(뒤뒤)한테 받을 수 있다
        if i != 0:
            if student[i]>1 and student[i-1]==0:
                student[i] -= 1
                student[i-1] += 1
        if i != n-1:
            if student[i]>1 and student[i+1]==0:
                student[i] -= 1
                student[i+1] += 1
    answer = n - student.count(0)
    return answer

import sys

n = int(sys.stdin.readline())
lost = list(map(int, sys.stdin.readline().split(", ")))
reserve = list(map(int, sys.stdin.readline().split(", ")))
print(solution(n, lost, reserve))