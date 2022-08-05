# combinations 패키지와 2중 for문 사용
from itertools import combinations

def solution(nums):
    answer = 0
    a = list(combinations(nums, 3))
    
    for i in range(len(a)):
        for j in range(2, sum(a[i]) - 1):
            if sum(a[i]) % j == 0:
                break
        else:
            answer += 1
    return answer
  
'''
# 3중 for문 사용
def solution(nums):
    answer = 0
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]
                
                for l in range(2, sum - 1):
                    if sum % l == 0:
                        break
                else:
                    answer += 1
    return answer
'''
