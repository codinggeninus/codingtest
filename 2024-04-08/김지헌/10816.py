def count_cards(N, cards, M, targets):
    card_count = {}
    # 카드별 개수를 저장하는 딕셔너리 생성
    for card in cards:
        if card in card_count:
            card_count[card] += 1
        else:
            card_count[card] = 1
    
    results = []
    # 각 타겟에 대해 상근이가 가지고 있는 카드의 개수를 찾음
    for target in targets:
        if target in card_count:
            results.append(card_count[target])
        else:
            results.append(0)
    
    return results

# 입력 받기
N = int(input())  # 상근이가 가지고 있는 숫자 카드의 개수
cards = list(map(int, input().split()))  # 숫자 카드에 적힌 정수들
M = int(input())  # 상근이가 구해야 할 숫자 카드의 개수
targets = list(map(int, input().split()))  # 상근이가 구해야 할 숫자 카드들

# 결과 출력
print(' '.join(map(str, count_cards(N, cards, M, targets))))
