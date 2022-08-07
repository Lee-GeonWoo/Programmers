def solution(price, money, count):
    p = 0
    
    for i in range(1, count+1):
        p += (price * i)

    return p-money if p-money > 0 else 0
