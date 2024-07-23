from itertools import combinations

heights = []
for _ in range(9):
	heights.append(int(input()))

heights.sort()
diff = sum(heights) - 100

sliced_heights = [value for value in heights if value < diff]

for item in combinations(sliced_heights, 2):
	if sum(item) == diff:
		for i in heights:
			if i in item:
				continue
			print(i)
		break