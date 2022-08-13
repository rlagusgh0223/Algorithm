n, m = map(int, input().split())
answer = []

def backTracking(depth):    # 백트래킹 알고리즘을 위한 재귀함수. 현재 수열의 길이를 인자로 받는다
    if depth==m:    # 현재 수열의 길이가 m이라면 출력하기 위한 변수이다. 현재 수열 출력
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):    # 1부터 n까지 반복
        answer.append(i)    # 현재 수열의 끝에 수 추가
        backTracking(depth+1)    # 수열에 수를 추가한 채로 현재 깊이 depth를 1증가시켜 백트래킹 함수 실행
        answer.pop()    # 수열의 끝에 있는 수 삭제

backTracking(0)    # 백트래킹 알고리즘의 현재 깊이를 0으로 하여 실행