# n=int(input())
# """
# 전줄꺼랑 안겹치게할것.
# 출력받고
# 2번쨰 줄부터 1번쨰줄에서 안겹치는애들중 최솟값을 더함
# 최종출력은 배열의 마지막이므로 n-1
# """
# arr=[]
# for _ in range(n):
#     arr.append(list(map(int,input().split())))
#
# for i in range(1,n):
#     arr[i][0]=min(arr[i-1][1],arr[i-1][2])+arr[i][0]
#     arr[i][1]=min(arr[i-1][0],arr[i-1][2])+arr[i][1]
#     arr[i][2]=min(arr[i-1][1],arr[i-1][0])+arr[i][2]
# print(min(arr[n-1]))
#
#
#























n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

for i in range(1,n):
    arr[i][0]=min(arr[i-1][1],arr[i-1][2])+arr[i][0]
    arr[i][1]=min(arr[i-1][0],arr[i-1][2])+arr[i][1]
    arr[i][2]=min(arr[i-1][1],arr[i-1][0])+arr[i][2]
print(min(arr[n-1]))



