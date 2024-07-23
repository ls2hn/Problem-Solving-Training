# 구름톤 챌린지 4일차 미션 - 완벽한 햄버거 만들기 

num_in = int(input())
flavor = input().split()   # split은 리스트를 반환한다! 
flavor = list(map(int, flavor))  # map(int, flavor) 출력하면 <map object at 0x7fc272e69e20>

front = flavor[:flavor.index(max(flavor)):]			# ! 배열명.index()
latter = flavor[flavor.index(max(flavor))::]		# !

if ( front == sorted(front)) and (latter == sorted(latter,reverse=True) ):
	print(sum(flavor))
else :
	print(0)

# sorted()함수는 sort된 리스트를 반환한다. / 리스트명.sort()는 그 리스트를 정렬시킨다. 반환값은 None이다.
# sorted(리스트명, reverse=True)는 내림차순 정렬한 리스트를 반환한다.

# list(reversed(리스트명))은 순서를 거꾸로 뒤집은 리스트를 반환한다. 
	# reversed(리스트명)의 출력값은 <list_reverseiterator object at 0x7f3088353730>

# 리스트 슬라이싱  flavor[1:-1:] 이거는 맨뒤 요소의 바로 앞 요소까지. -1 안넣으면 맨뒤 요소까지.
