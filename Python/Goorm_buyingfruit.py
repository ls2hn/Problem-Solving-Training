# 구름톤 챌린지 15일차 과일 구매문제 https://level.goorm.io/l/challenge/goormthon-challenge

N, K = map( int, input().split() )		# 과일의 개수 N, 가진 돈 K.
result = 0 					# 포만감 합계를 담을 것임
lst = []					# P(가격 및 과일조각의 개수),C/P(조각당 포만감) 값의 쌍을 가질 이차원 list
for _ in range(N) :
	tmp_lst = []				# 이차원 배열을 만들기 위해 사용될 list
	tmp_P, tmp_C = map( int, input().split() )
	tmp_lst.append(tmp_P)
	tmp_lst.append(int(tmp_C/tmp_P))
	lst.append(tmp_lst)			# P,C 값의 쌍을 갖는 이차원 list를 만듦

lst.sort(key=lambda x: -x[1])			# 각 원소의 C/P값을 기준으로 내림차순 정렬

for P, pieceC in lst:
	if P <= K :
		result += pieceC * P
		K -= P

	else : 		# P(조각개수) > K(가진 돈)인 경우
		result += pieceC * K
		K -= K
		
	if K==0 : break

print(result)


# 해설 코드
# N, K = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]	# P,C의 값 쌍을 이차원배열로 받음 - 깔끔한 한줄 코드 !

# arr.sort(key=lambda x : x[1] // x[0])				# C/P의 몫을 기준으로 정렬

# result = 0

# while K and arr:		# K(가진 돈)>0 and arr(list가 비어있으면 0)안에 요소 있을 때
# 	P, C = arr.pop()
	
# 	if K >= P:
# 		result += C
# 		K -= P
# 	else:
# 		result += C // P * K
# 		K = 0

# print(result)
