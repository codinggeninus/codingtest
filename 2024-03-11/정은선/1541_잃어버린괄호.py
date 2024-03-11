s = input()
arr = [] #양수와 음수 형태로 구분

number = '' #숫자 초기화
for i in range(len(s)):
    #연산자가 나올 경우 숫자 부분 추가, 초기화
    if s[i].isdigit() == False:
        arr.append(int(number))
        number = '' 
    number += s[i] #현재 문자 더해줌
    if i == len(s)-1: #마지막 숫자 처리
        arr.append(int(number))

result = arr[0] #계산 시작값
minus = False 
for i in range(1, len(arr)):
    #음수일 경우 그대로 더함
    if arr[i] < 0:
        result += arr[i]
        minus = True #음수가 나온 뒤로는 다 빼도록 계산
    else:
        if minus: #음수가 나온 뒤로는 앞 -와 묶어서 계산 가능
            result -= arr[i]
        else: #앞에 음수가 없는 경우에는 더함
            result += arr[i]

print(result)