import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

result = []
def back_tracking(i):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    
    for i in range(len(nums)):

        if nums[i] not in result:
            # 현재 수를 result에 추가
            result.append(nums[i])
            back_tracking(i+1)
            result.pop()


back_tracking(0)