# 손익분기점
import math

A, B, C = map(int, input().split())
if C <= B :
	print(-1)
else:
	X = A / (C-B)
	X = math.floor(X+1)
	print(X)
