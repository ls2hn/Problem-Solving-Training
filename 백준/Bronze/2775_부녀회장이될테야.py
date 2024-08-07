def calc(a, b):
	result = 0
	
	if a == 0:
		return b
	if dd[a][b] != 0:
		return dd[a][b]
	
	for i in range(1, b+1):
		result += calc(a-1, i)
	dd[a][b] = result
	return dd[a][b]

T = int(input())
for _ in range(T):
	k = int(input())
	n = int(input())

  # DP 리스트 잘못된 초기화
	# d = [0]*(n+1)
	# dd = []
	# for _ in range(k+1):
	# 	dd.append(d)
    
	# 올바르게 초기화하기 위해 개별 리스트를 생성
	dd = [[0] * (n + 1) for _ in range(k + 1)]
	
	dd[k][n] = calc(k,n)
	print(dd[k][n])
