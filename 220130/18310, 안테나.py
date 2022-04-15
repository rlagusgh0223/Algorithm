# 모범답안
# 중간에 있는 집에 설치하면 가장 적은 값을 낼 수 있다
import sys
n = int(sys.stdin.readline())   # 입력값 받을 변수와 리스트
x = list(map(int, sys.stdin.readline().split()))
x.sort()
print(x[(n-1)//2])





# 시간 초과
# ==============================================
# import sys
# n = int(sys.stdin.readline())   # 입력값 받을 변수와 리스트
# x = list(map(int, sys.stdin.readline().split()))
# x.sort()        # 거리가 동일한 값이 나올 경우 작은 값이 나온다고 했으므로 순서대로 정렬
# ans = [0] * n

# for i in range(len(x)):         # 입력받은 각 값의 주변 값들과의 거리 계산
#     for j in x:
#         ans[i] += abs(x[i]-j)

# X = ans[0]  # 가장 작은 값을 비교하기 위한 변수. 우선 제일 첫번째 값 저장
# cnt = 0     # 가장 작은값이 몇번째인지 체크할 변수
# for i in range(1, len(ans)):    # 현재 값보다 작은 값이 나올경우 작은값의 값과 리스트의 번호 저장
#     if X > ans[i]:
#         X = ans[i]
#         cnt = i
        
# print(x[cnt])   # 가장 작은 수가 있는 리스트의 번호 입력하여 출력