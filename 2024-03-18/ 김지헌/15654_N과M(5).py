def backtracking(nums, M, result):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for num in nums:
        if num not in result:  # 이미 선택된 숫자는 건너뜀
            backtracking(nums, M, result + [num])

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()  # 숫자를 오름차순으로 정렬

backtracking(nums, M, [])
