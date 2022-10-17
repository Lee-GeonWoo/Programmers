def solution(emergency):
    answer = [0] * len(emergency)
    for i in range(1, len(emergency)+1):
        answer[emergency.index(max(emergency))] = i
        emergency[emergency.index(max(emergency))] = 0
    return answer
