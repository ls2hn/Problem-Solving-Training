bar = 64
X = int(input())
answer = 0
while True:
	
	if X < bar:
		bar /= 2
	elif X > bar:
		answer += 1
		X -= bar
	else :
		answer += 1
		break

print(answer)

# 풀이 2
bar = 64
X = int(input())
bin_X = format(X, 'b')
answer = bin_X.count('1')
print(answer)
