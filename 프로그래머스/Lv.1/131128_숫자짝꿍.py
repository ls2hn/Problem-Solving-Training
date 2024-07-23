def solution(X, Y):
    from collections import Counter
    counter_x = Counter(X)
    counter_y = Counter(Y)
  
    common = []
    for digit in counter_x:
        if digit in counter_y:
            common.extend([digit] * min(counter_x[digit], counter_y[digit]))
          
    if not common:
        return "-1"
    common.sort(reverse=True)
  
    if common[0] == '0':
        return "0"
    
    return ''.join(common)
