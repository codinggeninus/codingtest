n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
#a 오름차순 b 내림차순 재배열
#b 재배열 불가라 하였으나 결국 결과는 동일
a.sort()
b.sort(reverse=True)

#a[i]*b[i]의 총합
total = 0
for i in range(n):
    total += a[i] * b[i]
    
print(total)