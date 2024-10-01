n, k = map(int, input().split())
arr = list(map(int, input().split()))

new_arr = []
for item in arr:
	new_arr.append([bin(item)[2:].count('1'), item])

new_arr.sort(reverse = True)
print(new_arr[k-1][1])
