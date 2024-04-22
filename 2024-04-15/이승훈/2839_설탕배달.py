"""
2839. 설탕 배달
"""
from sys import stdin

n = int(stdin.readline())

# 배달 가능한 5kg 단위의 주머니 개수를 구한다.
five_count = n // 5
answer = five_count

# 만약 5kg 단위의 설탕 주머니를 뺀 후 주머니가 남아 있거나
# 주어진 설망 주머니가 5kg보다 작은 경우
if n % 5 != 0:

    # 5kg 단위의 설탕 주머니 개수를 조정하며 N 킬로그램을 담을 수 있는지 탐색하는 과정이다.
    for cnt in range(five_count, -1, -1):

        # 현재 적재된 5kg 단위로 정확히 N 킬로그램을 담을 수 있다면
        # 3kg 단위의 주머니 개수를 더한다.
        if (n - 5 * cnt) % 3 == 0:
            answer += (n - 5 * cnt) // 3
            break

        # 만일 현재 적재된 5kg 단위로 정확히 N 킬로그램을 담을 수 없다면
        # 주머니의 개수를 하나 뺀다.
        answer -= 1

print(answer)
