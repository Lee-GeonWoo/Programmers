# 에라토스테네스의 체 활용
def solution(n):

    answer = [0, 0] + [1] * (n-1)         # [0, 0, 1, 1, 1, 1]
    
    for i in range(2, n+1):
        for j in range(i * 2, n+1, i):    
            answer[j] = 0                 # [0, 0, 1, 1, 0, 1]
    return answer.count(1)
  
  
'''
# timeout 뜬 코드
def solution(n):
    answer = 0
    
    for i in range(2, n+1):
        count = 0
        for j in range(2, i+1):
            if i % j == 0:
                count += 1
        if count == 1:
            answer += 1
    return answer
'''
