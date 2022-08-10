def solution(progresses, speeds):
    answer = []
    day = []
    
    for i in range(len(speeds)):
        count = 0        
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count += 1
        day.append(count)

    cnt = 1
    
    for j in range(len(day) - 1):
        if day[j] >= day[j + 1]:
            day[j + 1] = day[j]
            cnt +=1
        else:
            answer.append(cnt)
            cnt = 1
    answer.append(cnt)
    
    return answer
