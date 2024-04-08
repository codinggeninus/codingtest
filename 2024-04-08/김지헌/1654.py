def count_lan_cables(K, N, lan_cables, length):
    count = 0
    for cable in lan_cables:
        count += cable // length
    return count

def find_max_length(K, N, lan_cables):
    start = 1  # 최소 길이
    end = max(lan_cables)  # 최대 길이
    result = 0
    
    while start <= end:
        mid = (start + end) // 2  # 중간 길이
        
        # mid 길이로 만들 수 있는 랜선의 개수 계산
        count = count_lan_cables(K, N, lan_cables, mid)
        
        # 필요한 개수보다 많이 만들 수 있는 경우
        if count >= N:
            result = mid
            start = mid + 1  # 길이를 늘려 더 큰 길이로 시도
        else:
            end = mid - 1  # 길이를 줄여 더 작은 길이로 시도
    
    return result

# 입력 받기
K, N = map(int, input().split())  # 가지고 있는 랜선의 개수 K, 필요한 랜선의 개수 N
lan_cables = [int(input()) for _ in range(K)]  # 각 랜선의 길이

# 최대 길이 찾기
print(find_max_length(K, N, lan_cables))
