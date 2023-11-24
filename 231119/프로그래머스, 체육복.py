def solution(n, lost, reserve):
    answer = 0
    student = [1] * n
    for l in lost:
        student[l-1] -= 1
    for r in reserve:
        student[r-1] += 1
    for i in range(n):
        if i > 0:
            if student[i]==2 and student[i-1]==0:
                student[i] = 1
                student[i-1] = 1
        if i < n-1:
            if student[i]==2 and student[i+1]==0:
                student[i] = 1
                student[i+1] = 1
    answer = len(student) - student.count(0)
    return answer


import sys
n = int(sys.stdin.readline())
lost = list(map(int, sys.stdin.readline().split()))
reserve = list(map(int, sys.stdin.readline().split()))
print(solution(n, lost, reserve))