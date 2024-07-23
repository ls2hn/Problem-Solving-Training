def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] *= -1
    return sum(absolutes)

# 다른 분 코드 (List comprehension)
# def solution(absolutes, signs):
#     return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
