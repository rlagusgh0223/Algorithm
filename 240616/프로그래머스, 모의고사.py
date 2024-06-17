def solution(answers):
    # 각 수포자의 점수를 입력할 리스트
    # (번호를 입력할 편의를 위해 4개를 만든다)
    check = [0] * 4  
    # 수포자들의 패턴별로 리스트 작성
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 해당 순서의 점수가 수포자가 찍기로 한
    # 순서의 점수와 같다면 맞춘 개수 1 증가
    for i in range(len(answers)):
        if answers[i] == one[i%len(one)]:
            check[1] += 1
        if answers[i] == two[i%len(two)]:
            check[2] += 1
        if answers[i] == three[i%len(three)]:
            check[3] += 1
    m = max(check)
    # 수포자들 중 가장 많이 맞춘 문제만큼 맞춘사람 리턴
    return [i for i in range(4) if check[i]==m]


import sys

print(solution(list(map(int, sys.stdin.readline().split(",")))))
