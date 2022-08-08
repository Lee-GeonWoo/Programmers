def solution(seoul):

    for idx, person in enumerate(seoul):
        if person == 'Kim':
            answer = '김서방은 {}에 있다'.format(idx)
    return answer
