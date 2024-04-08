def check_notes(N, notes1, M, notes2):
    notes_set = set(notes1)  # 수첩 1에 있는 숫자들을 set으로 변환하여 빠른 검색을 위해 저장
    results = []
    for note in notes2:
        if note in notes_set:
            results.append(1)
        else:
            results.append(0)
    return results

# 테스트케이스 개수 입력
T = int(input())

# 각 테스트케이스에 대해 실행
for _ in range(T):
    # 수첩 1 정보 입력
    N = int(input())
    notes1 = list(map(int, input().split()))
    # 수첩 2 정보 입력
    M = int(input())
    notes2 = list(map(int, input().split()))
    
    # 결과 출력
    for result in check_notes(N, notes1, M, notes2):
        print(result)
