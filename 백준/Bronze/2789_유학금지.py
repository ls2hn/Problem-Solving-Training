cambridge = list('CAMBRIDGE')
user_input = list(input())

for item in user_input:
	if item in cambridge:
		user_input = [value for value in user_input if value != item]

# for item in user_input:  
# 	# 두 줄 아래에서 바뀐 user_input을 반영하여 리스트의 다음번째 index를 조회하므로 모든 글자를 조회하지 못함.
# 	if item in cambridge:
# 		user_input.remove(item)
		
	# 처음 나온 for문에서는 List Comprehension을 사용하여 새로운 user_input 리스트를 생성한다. 즉, 원래의 user_input을 변경하지 않고 새로운 리스트를 만든다.
	
	# 반면에 아래의 for문에서는 remove() 메서드를 사용하여 원래의 user_input 리스트를 직접 변경한다. 따라서 첫 번째 for 루프를 실행하는 동안 user_input이 변경되어, 원래의 리스트에서 요소가 제거되었기 때문에 두 번째 for 루프에서는 원래의 리스트의 길이보다 작아진 새로운 길이를 기준으로 반복이 이루어지게 된다.

print(''.join(user_input))


## 아래는 다른 분의 정답 코드
# a = input()
# for i in "CAMBRIDGE":
#     a = a.replace(i,"")
# print(a)
