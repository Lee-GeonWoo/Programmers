def solution(n):
    answer = ''
    
    while n > 0:
        answer += str(n % 3)
        n //= 3
        
    return int(answer, 3)


'''
# 나머지 계산법을 이용한 풀이
def solution(n):
    three = []
    answer = 0
    
    while n > 0:
        three.append(n%3)
        n //= 3
    
    three.reverse()
    
    for i in range(len(three)):
        answer += (three[i] * 3 ** i) 
    
    return answer
'''
