def solution(food):
    del food[0]
    arr = []
    value = 1
    
    food = list(map(int, food))
    
    for item in food :
        rep = item // 2
        for i in range(rep):
            arr.append(value)
        value+=1
    
    arr = list(map(str,arr))
    answer = ''.join(arr)
    answer += '0'
    answer += ''.join(list(reversed(arr)))
                  
    return answer
