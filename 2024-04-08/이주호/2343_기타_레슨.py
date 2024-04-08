n,m = map(int,input().split())
arr1=list(map(int,input().split()))
'''
블루레이에는 총 N개의 강의가 들어가는데, 
블루레이를 녹화할 때, 강의의 순서가 바뀌면 안 된다. 
즉, i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의도 같은 블루레이에 녹화해야 한다.

블루레이의 개수를 가급적 줄이려고 한다. 오랜 고민 끝에 강토는 M개의 블루레이에 모든 기타 강의 동영상을 녹화하기로 했다.
이때, 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 단, M개의 블루레이는 모두 같은 크기이어야 한다.

강토의 각 강의의 길이가 분 단위(자연수)로 주어진다. 이때, 가능한 블루레이의 크기 중 최소를 구하는 프로그램을 작성하시오.

아 강의길이의 합의 최소는 강의중 가장긴거, 길이합이 가장길다면 강의들의 총합이구나.
길이를 일단 더하게함. 그러다 미드값보다 커지면 자르기!


'''
lo,hi = max(arr1),sum(arr1)
while lo<=hi:
    count=1
    length=0
    mid=(lo+hi)//2

    for i in arr1:
        if length+i > mid:
            length=0
            count+=1
        length+=i
    if count<=m:
        answer = mid
        hi=mid-1
    else:
        lo=mid+1

print(answer)





