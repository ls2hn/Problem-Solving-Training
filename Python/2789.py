cambridge = list('CAMBRIDGE')
user_input = list(input())

for item in user_input:
	if item in cambridge:
		user_input = [value for value in user_input if value != item]
		
for item in user_input:
	if item in cambridge:
		user_input.remove(item)
		
print(''.join(user_input))


## 아래는 다른 분의 정답 코드
# a = input()
# for i in "CAMBRIDGE":
#     a = a.replace(i,"")
# print(a)
