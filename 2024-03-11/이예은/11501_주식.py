# 그리디, 실버2
# https://www.acmicpc.net/problem/11501

T = int(input())
for i in range(T):
    n = int(input())
    nums = list(map(int, input().split()))
    curr = nums[-1]
    answer = 0

    for j in range(n-1, -1, -1):  # n-1 ~ 0, 역순, 미래 주가에서 과거로
        if nums[j] < curr:
            answer += curr - nums[j]
        # num[j]값이 curr과 같거나 보다 큰 경우, 과거(num[j])에 주식을 파는 게 이득이기에 curr을 큰 값으로 대체
        else:
            curr = nums[j]
    print(answer)
