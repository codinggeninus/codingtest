import sys
input = sys.stdin.readline

def back_tracking(i):
    
    global result, k, s

    if len(result) == 6:
        print(' '.join(map(str, result)))
        return
    
    for i in range(i, k):
        if s[i] in result:
            continue
        
        result.append(s[i])
        back_tracking(i+1)
        result.pop()

while(True):
    array = list(map(int, input().split()))
    if array[-1] == 0:
        break

    k = array[0]
    s = array[1:]

    result = []
    back_tracking(0)
    print()    