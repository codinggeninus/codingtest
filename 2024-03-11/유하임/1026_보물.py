N = int(input())
array1 = list(map(int, input().split()))
array2 = list(map(int, input().split()))
array1.sort()
array2.sort(reverse=True)
result = 0
for i in range(N):
    result += array1[i] * array2[i]
print(result)
