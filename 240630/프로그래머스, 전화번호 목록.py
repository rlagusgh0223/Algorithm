def solution(phone_book):
    phone_book.sort()  # 이게 있어야 에러 안 난다. 정렬을 시키면 비슷한 인접한 번호들간의 접두사를 효율적으로 비교할 수 있다
    # startswith
    # 문자열이 특정 접두사로 시작하는지 여부를 확인하는 메서드
    # zip을 통해 두 리스트를 묶어준다
    # 이를 통해 각 요소와 그 다음 요소를 한 쌍으로 만든다
    # ex) phone_book = ["119", "97674223", "1195524421"]
    # 일 경우 아래와 같이 쌍이 만들어진다
    # [("119", "1195524421"), ("1195524421", "97674223")]
    for ph, b in zip(phone_book, phone_book[1:]):
        if b.startswith(ph):
            return False
    return True

import sys

phone_book = list(sys.stdin.readline().strip().split('","'))
print(solution(phone_book))