lst = []
for x in range(1,99) :
    for y in range(x+1,100):
        for z in range (y+1,101) :
            if x*x + y*y == z*z :
               lst.append(sum([x,y,z])) 
for e in lst:
    print(f"({e} )",end="")
