import math
for i in range(2,101):
    flag = 0
    k = math.sqrt(i)
    k = int(k)
    for j in range(2,k+1):
        if i % j == 0 :
            flag = 1
            break
    if flag == 0 :
        print(i)
    
