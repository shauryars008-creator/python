age=input("enter a age : ")
age=int(age)
name=input("Enter a name : ")
if (name=="XYZ"):
    if age<40:
        print("suitable")
    elif age>50:
        print("old")
    else:
        print("ok")
else:
    print("not known")
