def solution(n):
    s = str(n)
    answer = []
    
    for i in range(1, len(s) + 1):
        answer.append(int(s[-i]))
    return answer

  
'''  
def solution(n):
    return [int(i) for i in str(n)][::-1]
'''
