a, b, v = map(int, input().split())
#v-a값 이상일 경우 다음날에 a만큼 올라가면 도착
day = (v-a) // (a-b) + 1
#그러나 v-a를 a-b로 나눈 나머지가 0이 아니라면 v-a에 도달하기 위해 1일이 더 필요함
if (v-a) % (a-b) > 0:
    day += 1
print(day)