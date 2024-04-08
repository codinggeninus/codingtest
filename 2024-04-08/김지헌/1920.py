def search_numbers(N, A, M, B):
    # 배열 A를 set으로 변환하여 빠른 검색을 위해 저장
    A_set = set(A)
    results = []
    for num in B:
        # 배열 B의 각 정수에 대해 배열 A에 존재하는지 확인
        if num in A_set:
            results.append(1)
        else:
            results.append(0)
    return results

# 입력 받기
N = int(input())  # 배열 A의 크기
A = list(map(int, input().split()))  # 배열 A
M = int(input())  # 배열 B의 크기
B = list(map(int, input().split()))  # 배열 B

# 결과 출력
for result in search_numbers(N, A, M, B):
    print(result)
