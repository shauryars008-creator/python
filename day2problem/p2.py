lst = ["OK", "NOK", "hello", "hi"]
#4)
print(lst[-1],lst[-2],lst[0])
lst[-1] = "hello"
print(lst)
#5)
print(len(lst[1]))
#6)
print(lst[0:2] , lst[2::])
#7)
print(lst[::-1])
#8)
print(lst[::2])
#9)
for e in lst :
    print(e, end = " ")
print('\n')
#10)
for i,e in enumerate(lst) :
    print(f"length of {i} is {len(e)}")

