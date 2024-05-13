a,b,v = map(int,input().split())

# if (v-b) % (a-b) == 0:
#   print((v-b) // (a-b))
# else:
#   print((v-b)//(a-b)+1)

"""
가야할 거리 // 하루동안 갈 수 있는거리.
나머지가 없다면 낮동안 정상 도착
나머지가 있다면 밤중에 미끄러져 내려오기 때문에 하루가 더 걸림

Ceil = 올림으로 정수형으로 변환
"""
import math
print(math.ceil((v-b) / (a-b)))
