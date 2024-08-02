import math

num = int(input())
for _ in range(num):
	n, m = map(int, input().split())
	result = math.comb(m, n)
	print(result)
