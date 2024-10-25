def get_digits(num):
    digits = []
    while num>=1:
        digits.append(num % 10)
        num //= 10
    return digits

def sum_of_powers(digits, P):
    power_sum = 0
    for item in digits:
        power_sum += item**P
    return power_sum

def solve(A, P):
    sequence = [A]
    seen = set(sequence)      
    while True:
        digits = get_digits(sequence[-1])
        power_sum = sum_of_powers(digits, P)
        if power_sum in seen:   # 단순히 중복 여부를 확인할 때에는 집합 자료구조가 효율적. 하지만 index처럼 순서 개념이 포함되면 list 필요.
            return sequence.index(power_sum)
        sequence.append(power_sum)
        seen.add(power_sum)

A, P = map(int, input().split())
print(solve(A, P))
