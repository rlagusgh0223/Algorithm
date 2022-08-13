n, m = map(int, input().split())
answer = []

def backTracking(depth):
    if depth==m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):
        if i in answer:    # 현재 수열에서 다음에 추가하고자 하는 i값이 수열 안에 있다면 해당 부분을 지나가고 다음 i값으로 넘어간다
            continue

        answer.append(i)
        backTracking(depth+1)
        answer.pop()

backTracking(0)