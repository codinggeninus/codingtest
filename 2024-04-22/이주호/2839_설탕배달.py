n=int(input())
count = 0
while(n>=0):
    if n%5 ==0:
        count+=n//5
        print(count)
        break

    n=n-3
    count+=1
else:
    print(-1)

"""
섩탕배달

5로 나눠떨어지면 그렇게하고
아니면 3으로 계속 빼면서 카운트 올림
그러다 0보다 작아지면 배달하자로 -1 출력
"""