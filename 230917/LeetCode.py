# 정수 배열 번호가 부여됩니다.
# 이 배열로 게임을 하는 플레이어는 플레이어 1과 플레이어 2입니다.
# 플레이어 1과 플레이어 2가 교대로 게임을 시작하고 플레이어 1이 먼저 시작합니다.
# 두 플레이어는 모두 0의 점수로 게임을 시작합니다.
# 매 턴마다 플레이어는 배열의 끝에서 숫자(즉, nums[0] 또는 nums[nums.length - 1])
# 중 하나를 가져가서 배열의 크기를 1씩 줄입니다. 플레이어는 선택한 숫자를 점수에 추가합니다.
# 배열에 더 이상 요소가 없을 때 게임이 종료됩니다.
# 플레이어 1이 게임에서 이길 수 있다면 true로 반환합니다.
# 두 플레이어의 점수가 같다면 플레이어 1은 여전히 승자이며, 또한 true로 반환해야 합니다.
# 두 플레이어 모두 최적의 플레이를 하고 있다고 가정할 수 있습니다.


# 예 1:
# 입력 : 숫자 = [1,5,2]
# 출력: false
# 설명: 처음에는 플레이어 1이 1과 2 중 하나를 선택할 수 있습니다.
# 2(또는 1)를 선택하면 플레이어 2는 1(또는 2)과 5 중에서 선택할 수 있습니다. 플레이어 2가 5를 선택하면 플레이어 1은 1(또는 2)로 남게 됩니다.
# 따라서 선수 1의 최종 점수는 1 + 2 = 3이고, 선수 2는 5입니다.
# 따라서 플레이어 1은 절대 승자가 될 수 없으며 거짓을 반환해야 합니다.

# 예 2:
# 입력 : 숫자 = [1,5,233,7]
# 출력: true
# 설명: 플레이어 1이 먼저 1을 선택합니다. 그 다음 플레이어 2는 5와 7 중 하나를 선택해야 합니다. 플레이어 2가 어떤 번호를 선택하든 플레이어 1은 233을 선택할 수 있습니다.
# 마지막으로 플레이어 1이 플레이어 2(12)보다 점수(234)가 더 많으므로 True를 반환해야 플레이어 1이 이길 수 있습니다.

# 플레이어 1이 승리할 경우의 수가 있는데, 그건 생각하지 않고 플레이어 2가 가장 큰 값을 갖게 하는걸 어떻게 하지?
def DFS(x):
    global one, two, ans
    if len(lst) == 0:
        print(one, two)
        if sum(one) >= sum(two):
            ans = True
        return
    if x==0:
        # 첫번째 값 계산
        one.append(lst.popleft())
        DFS(1)
        lst.appendleft(one.pop())
        # 마지막 값 계산
        one.append(lst.pop())
        DFS(1)
        lst.append(one.pop())
    else:
        # 첫번째 값 계산
        two.append(lst.popleft())
        DFS(0)
        lst.appendleft(two.pop())
        # 마지막 값 계산
        two.append(lst.pop())
        DFS(0)
        lst.append(two.pop())

from collections import deque
import sys
lst = deque(list(map(int, sys.stdin.readline().split())))
one, two, ans = [], [], False
DFS(0)
if ans:
    print("true")
else:
    print("false")