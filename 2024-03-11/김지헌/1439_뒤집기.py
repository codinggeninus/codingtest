import sys
sys.stdin = open("뒤집기.txt","r")
#-------------------------------------
N = int(input())
L = list(str(N))
print(L)
count = 0
for i in range(len(L)-1):
    if L[i]!=L[i+1]:
        count+=1
print((count+1)//2)
