def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    zero = lottos.count(0)
    correct = 0
    
    for i in lottos:
        if i in win_nums:
            correct += 1
    answer.append(rank[zero+correct])
    answer.append(rank[correct])
    
    return answer
