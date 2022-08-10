def solution(phone_number):

    for s in range(len(phone_number) -4):
        phone_number = phone_number.replace(phone_number[s], '*')
    return phone_number
  
  
# 한 줄로 작성
'''
def solution(phone_number): 
    return "*" * (len(phone_number)-4) + phone_number[-4:]
''' 
