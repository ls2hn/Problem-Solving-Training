def solution(n, lost, reserve):
    # 여벌 체육복이 있는 학생이 도난당한 경우를 처리
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    reserve= list(reserve_set)
    lost = list(lost_set)

    count=0
    
    for item in lost:
        if front(item, reserve) == True:
            reserve.remove(item-1)
            count += 1
            continue
        elif back(item,reserve) == True:
            count+= 1
            reserve.remove(item+1)
    
    answer = n - len(lost) + count
    return answer
 
def front(k, reserve):  # k: 번호
    if k-1 in reserve:
        return True
    else:
        return False
 
def back(k, reserve):
    if k+1 in reserve:
        return True
    else:
        return False


# # 더 정제된 다른 코드
# def solution(n, lost, reserve):
#     # 여벌 체육복이 있는 학생이 도난당한 경우를 처리
#     reserve_set = set(reserve) - set(lost)
#     lost_set = set(lost) - set(reserve)
    
#     for item in reserve_set:
#         if item - 1 in lost_set:
#             lost_set.remove(item - 1)
#         elif item + 1 in lost_set:
#             lost_set.remove(item + 1)
    
#     answer = n - len(lost_set)
#     return answer
