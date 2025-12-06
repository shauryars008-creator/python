lst = ["OK", "NOK", "hello", "hi"]
counteven = 0
countodd = 0
tot = 0
for e in lst :
    if len(e)%2 == 0 :
        counteven += 1
    if len(e)%2 == 1 :
        countodd += 1
    tot += len(e)
    
print(f"""number of even strings : {counteven}
number of odd strings : {countodd}
Total length of all strings : {tot}""")