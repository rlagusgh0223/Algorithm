def solution(clothes):
    answer = 1
    cloth = Counter([c[1] for c in clothes])
    for c in cloth.values():
        answer *= (c+1)  # 옷을 안 입는 경우도 포함 ex) face 종류 중 아무것도 안 입을 수 있다)
    return answer-1  # 위의 식대로 하면 모두 안입는 경우도 포함되므로 제외한다(어느 한 부분은 입고 있어야 됨)



from collections import Counter  # 각 원소와 그 원소의 개수를 저장한다 ex) Counter({'headgear': 2, 'eyewear': 1})
import sys
n = int(sys.stdin.readline())
cloths = []
for i in range(n):
    x, y = sys.stdin.readline().split()
    cloths.append([x, y])
print(solution(cloths))


# 예제
# 3
# yellow_hat headgear
# blue_sunglasses eyewear
# green_turban headgear

# 3
# crow_mask face
# blue_sunglasses face
# smoky_makeup face