# https://www.acmicpc.net/problem/1292

a, b = map(int, input().split())
arr = []
j = 1
count = 0

while count < b+1:
	for _ in range(j):
		arr.append(j)
		count+=1
	j+=1

print(sum(arr[a-1:b]))
