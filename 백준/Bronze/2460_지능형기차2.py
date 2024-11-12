current = 0
current_max = 0

for _ in range(10):
	outof, into = map(int, input().split())
	current -= outof
	current += into
	if current > current_max:
		current_max = current

print(current_max)
