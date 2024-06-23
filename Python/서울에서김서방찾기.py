def solution(seoul):
    for entry in enumerate(seoul):
        if entry[1] == "Kim":
            key = entry[0]
            break
            
    answer = f'김서방은 {key}에 있다'
    return answer

# 다른 분들의 모범 코드
# def solution(seoul):
#     return "김서방은 {}에 있다".format(seoul.index('Kim'))

# def solution(seoul):
#     return f"김서방은 {seoul.index('Kim')}에 있다"

# def solution(seoul):
#     return ('김서방은 %d에 있다' %seoul.index('Kim'))
