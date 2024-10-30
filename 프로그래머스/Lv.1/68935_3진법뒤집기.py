# 풀이 1
def solution(n):
    s = []
    while n != 0:
        s.append(n % 3)
        n //= 3
    
    return int(''.join(map(str, s)), base=3)

# 풀이 2
def solution(n):
    # 1. 3진법 변환
    base_3 = ''
    while n > 0:
        n, remainder = divmod(n, 3)
        base_3 += str(remainder)
    
    # 2. 뒤집어진 3진법 문자열을 그대로 10진법으로 변환
    return int(base_3, 3)

#  https://buly.kr/2qXDomZ 파이썬 진수변환
# n진수 -> 10진수  int(string, base)
# 2, 8, 16진수는 bin(), oct(), hex() 함수를 지원한다.
# 10진수 -> n진수  int() 같은 함수가 없기 때문에 직접 코드작성 해야한다.
