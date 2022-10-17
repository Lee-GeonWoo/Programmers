def solution(spell, dic):
    spell.sort()
    s = ''.join(spell)
    
    for i in range(len(dic)):
        if s == ''.join(sorted(dic[i])):
            return 1
    return 2
