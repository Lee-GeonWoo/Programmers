def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x: x[n])

# 같은 글자의 경우 사전순으로 정렬해야하기 때문에 sort()로 사전순 정렬
# key를 n번째 인덱스로 지정하고 strings를 정렬
