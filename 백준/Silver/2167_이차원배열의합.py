import sys
input = sys.stdin.readline

# 입력받기
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# 누적 합 계산
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = (
            matrix[i - 1][j - 1] +
            prefix_sum[i - 1][j] +
            prefix_sum[i][j - 1] -
            prefix_sum[i - 1][j - 1]
        )

# 쿼리 처리
rep = int(input())
for _ in range(rep):
    i, j, x, y = map(int, input().split())
    result = (
        prefix_sum[x][y]
        - prefix_sum[i - 1][y]
        - prefix_sum[x][j - 1]
        + prefix_sum[i - 1][j - 1]
    )
    print(result)
