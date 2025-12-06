lst = [1,2,3,5,6]
num = len(lst)
print(f"Number of elements = {num}")

if 7 in lst :
    print("7 is present")
else :
    print("7 is not present")

if lst == [1,2,3] :
    print("same")
else :
    print("not same")

lst[0]=lst[0]+10
print(lst)
