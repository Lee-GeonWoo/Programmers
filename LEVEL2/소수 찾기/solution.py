# 타임 아웃 뜬 코드 (에라토스테네스의 체 방법)
'''
from itertools import permutations

def solution(numbers):
    answer = 0
    a = []
    
    for i in range(1, len(numbers)+1):
        a.append(list(map(''.join, permutations(numbers, i))))
    a = sum(a, [])
    a = list(set(map(int, a)))

    for num in a:
        prime = [0, 0] + [1] * (max(a) - 1)
        
        for i in range(2, num+1):
            for j in range(i*2, num+1, i):
                prime[j] = 0
        if prime[num] == 1:
            answer += 1
        
    return answer
'''

# 다른 사람의 코드
from itertools import permutations

def solution(numbers):
    answer = 0
    a = []
    
    for i in range(1, len(numbers)+1):
        a.append(list(map(''.join, permutations(numbers, i))))
    a = sum(a, [])
    a = list(set(map(int, a)))

    for num in a:
        if num == 2:
            answer += 1

        for j in range(2, num):
            if num % j == 0:
                break
            if j == num-1:
                answer += 1
    return answer
