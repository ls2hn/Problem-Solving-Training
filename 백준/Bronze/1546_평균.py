import statistics

N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
new = []
for item in scores:
    temp = item/M*100
    new.append(temp)

print(statistics.mean(new))

# 풀이 2
# N = int(input())
# scores = list(map(int, input().split()))
# M = max(scores)
# new = []
# for item in scores:
#     temp = item/M*100
#     new.append(temp)

# print(sum(new)/N)
