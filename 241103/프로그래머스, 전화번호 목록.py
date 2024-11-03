def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # startswith는 str에서만 동작한다
        # if phone_book[i+1].startswith(phone_book[i]):
        #     return False
        
        # 속도는 위의 코드와 아래 코드 비슷하다
        now = phone_book[i]
        if now == phone_book[i+1][:len(now)]:
            return False
    return True

import sys

pb = list(sys.stdin.readline().strip().split('","'))
print(solution(pb))