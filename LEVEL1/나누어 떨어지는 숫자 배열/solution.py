def solution(arr, divisor):
    answer = []
    
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)

'''
# 간결하게 작성
def solution(arr, divisor):
    return sorted([x for x in arr if x % divisor == 0]) or [-1]
'''
