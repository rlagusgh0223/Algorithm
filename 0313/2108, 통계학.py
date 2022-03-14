from collections import Counter    # 최빈값을 구하는 부분에서 빈도값을 구하기 위해 선언
import sys

n = int(sys.stdin.readline())
lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))

# 산술평균
# lst의 합을 lst의 길이로 나누어준 값
# 소수점 첫째자리를 기반으로 반올림
# 반올림은 round
print(round(sum(lst) / n))

# 중앙값
# 숫자의 개수가 홀수이므로 중앙 index 이용
lst.sort()    # lst를 오름차순으로 만들어서 숫자들의 중앙값을 찾게 한다
print(lst[n//2])

# 최빈값
# 가장 빈도수가 높은 숫자
# Counter는 빈도수를 찾아주며,
# most_common()은 숫자가 많은 순서대로 정렬해준다. 빈도수가 같으면 먼저 입력된 순서대로 출력한다
num = Counter(lst).most_common()    # 각 리스트의 빈도수를 출력

if len(num) > 1 and num[0][1] == num[1][1]:    # 여러개 있을때에는 최빈값 중 두번째로 작은 값을 출력
    print(num[1][0])
else:
    print(num[0][0])

# 범위
# 최댓값 - 최솟값
print(max(lst) - min(lst))