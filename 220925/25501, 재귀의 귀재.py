def recursion(s, l, r):
    global answer
    answer += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

import sys
T = int(sys.stdin.readline())
S = []
for i in range(T):
    S.append(sys.stdin.readline().rstrip())
for i in range(T):
    answer = 0
    print(isPalindrome(S[i]), answer)
# print('ABBA:', isPalindrome('ABBA'))
# print('ABC:', isPalindrome('ABC'))