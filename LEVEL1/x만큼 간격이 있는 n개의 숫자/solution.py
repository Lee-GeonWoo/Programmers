def solution(x, n):
    answer = []
    
    for i in range(1, n+1):
        num = x * i
        answer.append(num)
    return answer

  
# 간결하게 작성
'''
def solution(x, n):
    return [i * x for i in range(1, n+1)]
'''
