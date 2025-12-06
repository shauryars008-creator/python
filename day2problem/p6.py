inputl = []
output = []
i = 0
while i < 4 :
    inputl.append(int(input()))
    i += 1
output = [e*e for i,e in enumerate(inputl) if i%2 == 0]
print(output)
