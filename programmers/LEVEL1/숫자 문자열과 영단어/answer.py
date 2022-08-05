dict = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5',
        'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9', 'zero' : '0'}

def solution(s):

    for key, val in dict.items():
        if key in s:
            s = s.replace(key, val)
    return int(s)
