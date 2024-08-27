def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # 속도는 비슷하다
        # if phone_book[i+1].startswith(phone_book[i]):
        now = phone_book[i]
        if now == phone_book[i+1][:len(now)]:
            return False
    return True

import sys

print(solution(list(sys.stdin.readline().strip().split('", "'))))
