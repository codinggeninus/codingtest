# 각 호별 거주민 수를 저장할 2차원 배열 생성
apartment = [[0] * 15 for _ in range(15)]

# 0층의 각 호별 거주민 수 초기화
for i in range(15):
    apartment[0][i] = i

# 각 층의 각 호별 거주민 수 계산
for i in range(1, 15):
    for j in range(1, 15):
        apartment[i][j] = apartment[i][j-1] + apartment[i-1][j]

# 테스트 케이스의 수 입력
T = int(input())

# 각 테스트 케이스에 대해 거주민 수 출력
for _ in range(T):
    k = int(input())  # 층
    n = int(input())  # 호
    print(apartment[k][n])
