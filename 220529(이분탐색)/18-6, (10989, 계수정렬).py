import sys
n = int(sys.stdin.readline())
count_sort = [0] * 10001    # 계수정렬을 위한 배열
for i in range(n):    # 계수정렬. 입력받은 수가 몇개인지 체크
    count_sort[int(sys.stdin.readline())] += 1
for i in range(10001):
    if count_sort[i] != 0:    # 해당 계수의 등장횟수가 0이 아니라면
        for j in range(count_sort[i]):    # 등장횟수만큼 계수 i를 출력한다
            print(i)
