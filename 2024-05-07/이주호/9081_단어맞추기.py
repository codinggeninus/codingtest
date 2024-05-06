import sys
input =sys.stdin.readline


"""
단어의 뒤에서부터 확인
맨뒤랑 작은 것 중 가장 가까운거랑 그 사이에서 확인 후 변경진행
이후 바뀐 단어 출력 

"""
def function1(word):
  for i in range(len(word)-1,0,-1):
    if word[i-1]<word[i]:
      for j in range(len(word)-1,i-1,-1):
        if word[i-1]<word[j]:
          word[i-1],word[j] = word[j],word[i-1]
          return (word[:i]+(word[i:][::-1]))
  return word
"""테스트에 대해 입력 후 단어에 대한 정렬 후 출력"""
n=int(input())
for _ in range(n):
  arr = list(input().strip())
  result = ''.join(function1(arr))
  print(result)