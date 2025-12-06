str = input("Give input aaabbbbaaac : ")
output=""
for e in str :
    if e not in output :
        output += e 
print(output)