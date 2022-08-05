def solution(numbers):
    return 45 - sum(numbers)

'''
# for문을 이용한 방법
def solution(numbers):
    answer = 0
    
    for i in range(1, 10):
        if i not in numbers:
            answer += i
    return answer
'''
