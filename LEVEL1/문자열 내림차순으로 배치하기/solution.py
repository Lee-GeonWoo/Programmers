def solution(s):
    answer = list(s)
    answer.sort(reverse=True)
    answer = ''.join(answer)
    
    return answer

'''
# 한 줄로 표현
def solutions(s):
    return ''.join(sorted(s)[::-1])
'''
