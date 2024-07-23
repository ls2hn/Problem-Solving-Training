# https://www.acmicpc.net/problem/1157
from collections import Counter

word = input().strip().upper()  # 공백을 제거하고 대문자로 변환

common = Counter(word).most_common()  # 알파벳의 빈도수를 계산하여 내림차순으로 정렬된 리스트 생성

# 가장 빈도수가 높은 값이 여러 개 있는지 확인
if len(common) > 1 and common[0][1] == common[1][1]:
    print('?')
else:
    print(common[0][0])
