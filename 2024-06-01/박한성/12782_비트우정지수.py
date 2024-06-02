T = int(input())
for _ in range(T) :
    a,b = input().split()
    numa = 0
    numb = 0
    for i in range(len(a)):
        if a[i] == '1' and b[i] == '0' :
            numa += 1
        elif b[i] == '1' and a[i] == '0' :
            numb += 1
    print(max(numa,numb))