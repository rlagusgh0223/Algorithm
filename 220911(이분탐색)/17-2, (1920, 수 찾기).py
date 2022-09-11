n = int(input())
a = list(map(int, input().split()))
a.sort()  # 이분탐색으로 이용하기 위해 a를 오름차순으로 정렬

def binarySeach(target):  # 이분탐색. 인자로는 b의 원소
    start = 0
    end = n - 1
    while start<=end:
        mid = (start+end) // 2
        if a[mid] == target:  # a[mid]가 찾고자 하는 b의 원소와 같다면 1 출력하고 함수 종료
            print(1)
            return
        elif a[mid]<=target:  # a[mid]가 찾고자 하는 b의 원소보다 작다면 start 재지정
            start = mid + 1
        else:  # a[mid]가 찾고자 하는 b의 원소보다 크다면 end값 재지정
            end = mid - 1
    print(0)  # 못 찾은 경우 0을 출력하고 함수 종료
    return

m = int(input())
b = list(map(int, input().split()))
for i in range(m):
    binarySeach(b[i])