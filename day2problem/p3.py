import random
lst = []
i = 0
while i<10 :
    lst.append(random.randint(10,50))
    i+=1
print(lst)
print(f"The sum of all elements is : {sum(lst)}")