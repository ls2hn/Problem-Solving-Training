def solution(n):
    import math
    X = math.sqrt(n)
    if X%1 == 0 :
        answer = (X+1)**2 
    else:
        answer = -1
    return answer

# 다른 분 코드 참고
# def solution(n):
#     return n == int(n**.5)**2 and int(n**.5+1)**2 or -1

# import math
# def solution(n):
#     # 함수를 완성하세요
#     return -1 if not math.sqrt(n).is_integer() else (math.sqrt(n)+1)**2
