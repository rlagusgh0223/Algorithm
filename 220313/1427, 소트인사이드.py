import sys
n = list(map(int, sys.stdin.readline().rstrip()))

# 방법1 sort() 사용
# sort()는 print()안에 넣으면 none이 나온다
# n.sort(reverse=True)    # reverse=True는 내림차순 의미
# print(n)

# 방법2 sorted() 사용
# sorted는 print()에 넣어서 바로 해도 된다
# print(sorted(n, reverse=True))
# m = sorted(n, reverse=True)    # 백준 사이트에서 제기한대로 결과 나오게 하려면 이렇게 해야된다

# 방법3 퀵 정렬을 이용해서 풀기
def quick(array):
    global n
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]    # 피벗은 첫 번째 원소
    tail = array[1:]    # 피벗을 제외한 리스트

    left = [x for x in tail if x>=pivot]    # 분할된 왼쪽 부분
    right = [x for x in tail if x<pivot]    # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick(left) + [pivot] + quick(right)

m = quick(n)

# 결과는 이걸로 도출한다 in 내용만 바꾸면 됨
for i in m:
    print(i, end='')