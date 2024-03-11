N = input()

new = N.split("-")
result_con = []
new_2 = 0
for i in new:
    if '+' in i:
        temp = 0
        new_2 = i.split('+')
        for j in new_2:
            temp += int(j)
        result_con.append(temp)
    else:
        result_con.append(int(i))
        
result = result_con[0]
for i in range(1,len(result_con)):
    result -= result_con[i]
    
print(result)
