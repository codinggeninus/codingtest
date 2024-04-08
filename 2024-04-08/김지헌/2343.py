def count_bluray(N, M, lengths, size):
    count = 1  # 처음에는 하나의 블루레이에 모든 강의를 녹화한다고 가정
    total_length = 0
    
    for length in lengths:
        # 블루레이에 녹화할 수 있는 경우
        if total_length + length > size:
            count += 1
            total_length = length
        else:
            total_length += length
    
    return count

def find_min_bluray_size(N, M, lengths):
    start = max(lengths)  # 강의 중 가장 긴 길이부터 시작
    end = sum(lengths)  # 모든 강의 길이의 합이 최대 블루레이 크기
    result = 0
    
    while start <= end:
        mid = (start + end) // 2  # 중간 크기로 블루레이 크기 시도
        
        # mid 크기로 녹화할 수 있는 블루레이의 개수 계산
        count = count_bluray(N, M, lengths, mid)
        
        # M개의 블루레이에 모든 강의를 녹화할 수 있는 경우
        if count <= M:
            result = mid
            end = mid - 1  # 크기를 줄여 더 작은 크기로 시도
        else:
            start = mid + 1  # 크기를 늘려 더 큰 크기로 시도
            
    return result

# 입력 받기
N, M = map(int, input().split())  # 강의의 수 N, 블루레이의 개수 M
lengths = list(map(int, input().split()))  # 각 강의의 길이

# 최소 블루레이 크기 찾기
print(find_min_bluray_size(N, M, lengths))
