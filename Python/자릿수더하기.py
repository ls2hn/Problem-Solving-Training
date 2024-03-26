import math

def solution(n):
    values = []
    
    while n :         # n이 0이 되면 멈춤.
        values.append(n % 10)
        n = math.floor(n/10)
    
    answer = sum(values)
    return answer
