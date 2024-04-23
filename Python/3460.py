# 이진수
#내 코드
T = int(input())
for _ in range(T):
	n = int(input())
	bi_n = format(n, 'b')
	index = 0
	
	for i in range(len(bi_n)-1, -1, -1):
		if bi_n[i] == '1':
			print(index, end=' ')
		index += 1

# 다른 분 거
# T = int(input())
# for _ in range(T):
#   n = int(input())
#   cnt=0
#   while n:
#     if n%2:
#       print(cnt, end=" ")
#     n //= 2
#     cnt+=1
