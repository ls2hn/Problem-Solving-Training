def solution(a, b):
    answer=0
    if a<=b:
        for i in range(a, b+1):
            answer += i
    else:
        for i in range(b, a+1):
            answer +=i
            
    return i

# # 참고 1
# def solution(a, b):
#     if a > b:
#         a, b = b, a
#     return sum(range(a, b + 1))

# # 참고 2
# def solution(a, b):
#     return (abs(a-b)+1)*(a+b)//2

# # 참고 3
# def solution(a, b):
#     return sum(range(min(a, b), max(a, b)+1))

# # 참고 4
# def solution(a, b):
#     return sum(range(a,b+1) if a <= b else range(b,a+1))

# # 참고 5
# def solution(a, b):
#     if(a>b):
#         return solution(b,a)
#     return sum([i for i in range(a,b+1)])
