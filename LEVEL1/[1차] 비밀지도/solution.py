def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        map = bin(arr1[i] | arr2[i])
        map = str(map[2:].zfill(n))
        map = map.replace('1', '#')
        map = map.replace('0', ' ')
        
        answer.append(map)     
    return answer
  
# bin과 |(or)를 활용한 bit 연산을 잘 해야한다
# zfill(n)은 n만큼의 길이로 2진수로 변환하고 남는 공간은 0으로 채운다.
