def find_closest_zero(N, solutions):
    left = 0
    right = N - 1
    min_diff = float('inf')  # 초기값을 무한대로 설정
    
    # 두 용액의 특성값 차이가 가장 작은 경우 찾기
    while left < right:
        sum_val = solutions[left] + solutions[right]  # 두 용액의 합
        
        # 특성값이 0에 더 가까운 경우 찾은 경우
        if abs(sum_val) < min_diff:
            min_diff = abs(sum_val)
            result = (solutions[left], solutions[right])
        
        # 합이 0보다 작거나 같으면 왼쪽 포인터를 오른쪽으로 이동
        if sum_val <= 0:
            left += 1
        # 합이 0보다 크면 오른쪽 포인터를 왼쪽으로 이동
        else:
            right -= 1
    
    return result

# 입력 받기
N = int(input())  # 전체 용액의 수
solutions = list(map(int, input().split()))  # 용액의 특성값

# 특성값이 0에 가장 가까운 용액의 두 개의 특성값 출력
result = find_closest_zero(N, solutions)
print(result[0], result[1])
