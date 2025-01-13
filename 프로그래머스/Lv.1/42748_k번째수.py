# 1
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

# 2
def solution(array, commands):
    answer = []
    for c in commands:
        answer.append(sorted(array[c[0]-1:c[1]])[c[2]-1])
    
    return answer
