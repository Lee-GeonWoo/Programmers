def solution(s):
    s = s.lower()
    num_p, num_y = 0, 0
    
    for letter in s:
        if letter == 'p':
            num_p += 1
        elif letter == 'y':
            num_y += 1            
    return True if num_p == num_y else False
