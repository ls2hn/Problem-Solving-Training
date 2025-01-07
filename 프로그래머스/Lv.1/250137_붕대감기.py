def solution(bandage, health, attacks):
    attack_num = 0
    in_a_row = 0
    hp = health
    
    for second in range(1, attacks[-1][0]+1):
        
        if in_a_row > 0:
            hp += bandage[1]
        if in_a_row == bandage[0]:
            hp += bandage[2]
            in_a_row = 0
        if hp > health:  # 최대체력
            hp = health
        in_a_row +=1
        
        # 공격당했을 시
        if attacks[attack_num][0] == second:
            hp -= attacks[attack_num][1]
            in_a_row = 0
            attack_num += 1
        # print('시간 : ', second, ' 현재체력 : ', hp, ' 연속 성공 : ', in_a_row)
        if hp <= 0:   # 죽음
            return -1
    answer = hp
    return answer
