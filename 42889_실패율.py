from collections import Counter

def solution(N, stages):
    stages_cnt = Counter(stages)
    total_users = len(stages)
    fail_rate = []
    
    for i in range(1, N+1):
        current_stage_users = stages_cnt[i]
        if total_users > 0:
            rate = current_stage_users / total_users
        else:
            rate = 0 
        fail_rate.append((i, rate))
        total_users -= current_stage_users
    sorted_fail_rate = sorted(fail_rate, key=lambda x: (-x[1], x[0]))
    
    return [stage for stage, _ in sorted_fail_rate] 
