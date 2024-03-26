def solution(s):
    
    p = y = 0
    
    for item in s:
        if (item=='p') or (item=='P') :
            p+=1
        if (item=='y') or (item=='Y') :
            y+=1

    return p==y
