def solution(ingredient):
    answer = 0
    stack = []
    
    for ing in ingredient:
        stack.append(ing)
        # 마지막 4개만 확인하여 패턴 검사
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            stack[-4:] = []  # 패턴 제거
            answer += 1
    
    return answer
