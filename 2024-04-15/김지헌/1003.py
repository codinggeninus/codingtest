# 시간초과 발생 때문에 미리 0부터 40까지의 피보나치 수열을 만들고 시작
list=[0,1]
def fibonacci(a,k):
    if(k==0):
        return
    list.append(list[a]+list[a+1])
    fibonacci(a+1,k-1)
    
fibonacci(0,40)


def main(n):
    k=0
    while(k!=n):
        k+=1
        t = int(input())
        if(t==0):
            print(1,0)
            continue
        print(list[t-1],list[t])

a = int(input())
main(a)
