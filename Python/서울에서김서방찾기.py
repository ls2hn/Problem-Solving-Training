def solution(seoul):
    for entry in enumerate(seoul):
        if entry[1] == "Kim":
            key = entry[0]
            break
            
    answer = f'김서방은 {key}에 있다'
    return answer
