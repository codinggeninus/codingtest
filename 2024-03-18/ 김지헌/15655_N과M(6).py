def backtracking(nums, M, result):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    
    for i, num in enumerate(nums):
        # 이전에 선택한 수보다 큰 수만 선택
        if not result or num > result[-1]:
            backtracking(nums[i+1:], M, result + [num])

N, M = map(int, input().split())
nums = sorted(map(int, input().split()))  # 입력으로 주어진 숫자를 오름차순으로 정렬

backtracking(nums, M, [])
