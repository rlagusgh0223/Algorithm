# 모범답안
def solution(s):
    answer = []
    word = dict()
    for i in range(len(s)):
        if s[i] not in word:
            answer.append(-1)
        else:
            answer.append(i - word[s[i]])
        word[s[i]] = i
    return answer



import sys
s = sys.stdin.readline().strip()
print(solution(s))

def solutions(s):
    answer = []
    word = {'a':-1,'b':-1,'c':-1,'d':-1,'e':-1,'f':-1,
            'g':-1,'h':-1,'i':-1,'j':-1,'k':-1,'l':-1,
            'm':-1,'n':-1,'o':-1,'p':-1,'q':-1,'r':-1,
            's':-1,'t':-1,'u':-1,'v':-1,'w':-1,'x':-1,'y':-1,'z':-1}
    for i in range(len(s)):
        if word[s[i]] == -1:
            answer.append(-1)
        else:
            answer.append(i - word[s[i]])
        word[s[i]] = i
    return answer