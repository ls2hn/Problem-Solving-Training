# 내가 풀던 건 틀려서 남 코드만 학습
#다른분코드1
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter

# #다른분코드2
# def solution(s):
#     answer = []

#     s1 = s.lstrip('{').rstrip('}').split('},{')

#     new_s = []
#     for i in s1:
#         new_s.append(i.split(','))

#     new_s.sort(key = len)

#     for i in new_s:
#         for j in range(len(i)):
#             if int(i[j]) not in answer:
#                 answer.append(int(i[j]))

#     return answer

# #다른분코드3
# def solution(s):
#     # {{, }}를 제거 후 },{ 으로 나누기
#     data = s[2:-2].split("},{")
#     # 길이 별로 오름차순 정렬
#     data = sorted(data, key=lambda x: len(x))
#     answer = []
#     for item in data:
#         # 각각의 원소로 분류 후
#         item = list(map(int, item.split(",")))
#         for value in item:
#             # 포함되어 있지 않으면 input
#             if value not in answer:
#                 answer.append(value)
#     return answer

# #다른분코드4
# from collections import Counter
# def solution(s):
#     new_s = [sss.replace('{','').replace('}','') for sss in s.split(',')]
#     return [int(c[0]) for c in sorted(Counter(new_s).items(), key = lambda x: x[1],reverse=True )]

# #다른분코드5  참고로 key는 따로 안넣어주고 그냥 sorted(s)해도 된다.
# def solution(s):
#     s = eval(s.replace("{", "[").replace("}", "]"))
#     answer = list({num:0 for k in sorted(s, key=lambda x: len(x)) for num in k}.keys())
#     return answer
