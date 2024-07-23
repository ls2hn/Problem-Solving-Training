# 코드업  https://codeup.kr/problem.php?id=6092
from collections import Counter
 
rollbook = []
n = int(input())
strange = input().split(' ')
 
counter_strange = Counter(strange)
list_counter_strange = list(counter_strange)
list_counter_strange.sort()
 
for i in range(1, 24):
	if str(i) in list_counter_strange:
		rollbook.append(str(counter_strange[str(i)]))
	else:
		rollbook.append('0')
 
answer = ' '.join(rollbook)
print(answer)

# 예시 코드

# n = int(input())
# a = input().split()
 
# for i in range(n) :
#   a[i] = int(a[i])   # a에 순서대로 저장되어있는 각 값을 정수로 변환해 다시 저장
 
# d = []
# for i in range(24) :
#   d.append(0)
 
# for i in range(n) :    # 번호를 부를 때마다, 그 번호에 대한 카운트 1씩 증가
#   d[a[i]] += 1
 
# for i in range(1, 24) :  # 카운트한 값을 공백을 두고 출력
#   print(d[i], end=' ')
