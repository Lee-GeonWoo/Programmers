def solution(arr):
    
    if len(arr) != 1:
        arr.remove(min(arr))
    else:
        arr.pop()
        arr.append(-1)
    return arr
