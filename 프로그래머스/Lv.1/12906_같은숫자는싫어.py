# 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    s = []      # s는 stack으로 쓸 것임
    for item in arr:
        if not s or s[-1] != item:    # s가 비어있거나 마지막요소가 item이 아니면
            s.append(item)
    return s
