def solution(n):
    answer = []
    n = str(n)
    
    for i in range(len(n)):
        answer.append(n[i])
    
    answer.sort(reverse=True)
    return int(''.join(answer))
  
  
# 다른 사람의 풀이
'''
def solution(n):
    a = list(str(n))
    a.sort(reverse=True)
    
    return int(''.join(a))
'''
