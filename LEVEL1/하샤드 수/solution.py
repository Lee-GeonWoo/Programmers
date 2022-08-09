def solution(x):
    a = []
    x = str(x)
    
    for i in range(len(x)):
        a.append(int(x[i]))

    return True if int(x) % sum(a) == 0 else False 
