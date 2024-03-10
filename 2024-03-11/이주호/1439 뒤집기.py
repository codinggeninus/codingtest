n = input()

sum1=0
for i in range(len(n)-1):
    if(n[i]!=n[i+1]):
        sum1+=1

print(sum1+1//2)
