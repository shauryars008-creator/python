strr = "Hello World and Hello Earth"
lst = []
lstcnt = []
for e in strr.split() : 
    for i in e :
        if i in lst :
            for j,k in enumerate(lst) :
                if k == i :
                    index = j
            lstcnt[index] +=1
        else :
            lst.append(i)
            lstcnt.append(1)
for i in range(len(lst)) :
    print(f"{lst[i]} = {lstcnt[i]}")
        
    
