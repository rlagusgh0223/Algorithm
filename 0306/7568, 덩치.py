import sys
n = int(sys.stdin.readline())
man = []
check = [1] * n    # 순서를 계산할때는 1부터 시작하니까 1로 인원수만큼 초기화

for i in range(n):    # 각 사람의 체격 입력
    man.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):    # 체격 순위 측정할 사람 정하는 반복문
    for j in range(n):    # 측정할 사람과 비교할 사람 정하는 반복문
        if i == j:    # 만약 본인일 경우 이번 순서는 끝
            continue
        if man[i][0] < man[j][0] and man[i][1] < man[j][1]:    # 몸무게와 키가 모두 비교하는 사람보다 작을 경우
            check[i] += 1    # 등수는 하나 증가
        
for i in range(n):    # 틀렸다고 나오는데 출력 형식이 잘못된건지 확인
    print(check[i], end=' ')