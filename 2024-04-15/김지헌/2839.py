# 설탕의 무게 입력
N = int(input())

# 5킬로그램 봉지로 최대한 채우고, 남은 무게를 3킬로그램 봉지로 채우는 방식으로 구현

# 5킬로그램 봉지의 최대 개수 구하기
count_5kg = N // 5

# 남은 설탕 무게 구하기
remainder = N % 5

# 남은 무게가 3킬로그램으로 딱 나눠진다면
if remainder % 3 == 0:
    # 5킬로그램 봉지와 3킬로그램 봉지의 합이 최소이므로 총 봉지의 수 출력
    print(count_5kg + remainder // 3)
else:
    # 5킬로그램 봉지를 하나씩 줄여가면서 남은 무게를 3킬로그램 봉지로 채우기
    while count_5kg > 0:
        count_5kg -= 1
        remainder += 5  # 5킬로그램 봉지 하나를 줄였으므로 남은 무게에 5를 더함
        # 남은 무게가 3킬로그램으로 딱 나눠진다면
        if remainder % 3 == 0:
            # 5킬로그램 봉지와 3킬로그램 봉지의 합이 최소이므로 총 봉지의 수 출력
            print(count_5kg + remainder // 3)
            break
    else:
        # 5킬로그램 봉지를 모두 사용했는데도 남은 무게를 3킬로그램 봉지로 채울 수 없는 경우 -1 출력
        print(-1)
