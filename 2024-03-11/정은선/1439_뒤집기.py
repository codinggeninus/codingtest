s = input()

#연결된 0과 1의 개수 배열
num = [0, 0]
#문자열 첫 숫자 추가
num[int(s[0])] = 1

#현재와 다음이 다를 경우 +1
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        num[int(s[i+1])] += 1

#배열의 최솟값 출력
print(min(num))