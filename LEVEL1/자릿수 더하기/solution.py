def solution(n):
    s = str(n)
    answer = []
    
    for i in range(len(s)):
        answer.append(int(s[i]))    
    return sum(answer)
  
'''
# 한 줄 작성
def solution(n):
    return sum(int(i) for i in str(n))
'''
