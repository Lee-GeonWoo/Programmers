def solution(s):
    answer = ''
    
    if len(s) % 2 == 0:
        answer = s[(len(s) // 2) - 1 : (len(s) // 2) + 1]
    else:
        answer = s[len(s) // 2]
    return answer
  
# or (한 줄로 표현)
'''
def solution(s):
    return s[(len(s) // 2) - 1 : (len(s) // 2) + 1] if len(s) % 2 == 0 else s[len(s) // 2]
'''
