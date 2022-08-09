def solution(n, m):
    answer = []  
    temp1, temp2 = [], []

    for i in range(1, n+1):
        if n % i == 0 and m % i == 0:
                temp1.append(i)
    
    for j in range(1, n * m + 1):
        if j % n == 0 and j % m == 0:
                temp2.append(j)
                
    answer.append(max(temp1))
    answer.append(min(temp2))
    
    return answer



# math의 gcd() 함수 활용
'''
from math import gcd

def solution(n, m):
    answer = [gcd(n, m), lcm(n, m)]
    return answer

def lcm(a,b):
    return (a * b) // gcd(a,b)
'''
