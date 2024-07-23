# 프로그래머스 https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    rep = zeros = 0

    while s != '1' :
        cnt = s.count('0')
        s = s.replace('0', '', cnt)

        zeros += cnt
        rep += 1
        
        s = format(len(s), 'b')
    
    answer = [rep, zeros]
    return answer
