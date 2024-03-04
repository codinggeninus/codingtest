#동전 n종류, 가치의 합 k
n, k = map(int, input().split())
arr = [] #동전의 가치 배열
for _ in range(n):
    arr.append(int(input()))
#내림차순으로 정렬
arr.sort(reverse=True)

total = 0 #사용한 동전의 개수

#동전의 가치가 남은 k보다 작은 경우 k를 i로 나눈 몫 a, 나머지 k
for i in arr:
    if i <= k:
        a, k = divmod(k, i)
        total += a #동전의 개수에 몫 더하기
        if k == 0: #나머지가 0이 되면 종료
            break
