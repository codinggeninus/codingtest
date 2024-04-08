def cut_trees(N, M, heights):
    start = 0  # 절단기 높이의 최솟값
    end = max(heights)  # 절단기 높이의 최댓값
    result = 0
    
    while start <= end:
        mid = (start + end) // 2  # 절단기 높이의 중간값
        
        total_length = 0
        for height in heights:
            if height > mid:
                total_length += height - mid
        
        # 적어도 M미터의 나무를 가져갈 수 있는 경우
        if total_length >= M:
            result = mid
            start = mid + 1  # 높이를 높여 더 많이 잘라냄
        else:
            end = mid - 1  # 높이를 낮춰 더 적게 잘라냄
            
    return result

# 입력 받기
N, M = map(int, input().split())  # 나무의 수 N과 필요한 나무의 길이 M
heights = list(map(int, input().split()))  # 각 나무의 높이

# 결과 출력
print(cut_trees(N, M, heights))
