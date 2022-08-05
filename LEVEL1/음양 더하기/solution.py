def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    return answer


'''
# zip을 이용한 방식
def solution(absolutes, signs):
    answer = 0
    
    for abs, sign in zip(absolutes, signs):
        if sign == True:      # 또는 if sign:
            answer += abs
        else:
            answer -= abs
    return answer
'''
